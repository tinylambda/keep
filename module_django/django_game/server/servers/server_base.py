import asyncio
import binascii
import json
import logging
import os
import typing
import urllib.parse

import aioelasticsearch
import aioredis

from operator import itemgetter
from channels.layers import get_channel_layer
from django.conf import settings

from .mixins.es import EntityESOperationMixin
from ..consumers import GameConsumer


class ServerBase(EntityESOperationMixin):
    ID_NAME = 'id'
    DB_NAME = 'default'

    def __init__(self, min_tick_interval=1.0):
        self.server_name = self.__class__.__name__
        self.min_tick_interval = min_tick_interval

        self._main_task_callables: typing.List[typing.Callable] = []
        self.main_tasks: typing.List[asyncio.Task] = []

        self.managed_tasks: typing.Dict[typing.AnyStr, asyncio.Task] = {}
        self.managed_task_change_lock: asyncio.Lock = asyncio.Lock()

        self.loop = asyncio.get_event_loop()
        self.result_q: asyncio.Queue = asyncio.Queue()
        self.channel_layer = get_channel_layer()

        self.server_task_queue_service = None
        self.storage = None

        self.server_started = asyncio.Future()
        self.server_closing = asyncio.Future()
        self.server_closed = asyncio.Future()

        self._worker_id = None
        self.result_getter = itemgetter('group', 'content')

        self.main_task: asyncio.Task = None

    @property
    def worker_id(self):
        if not self._worker_id:
            random_bytes = binascii.hexlify(os.urandom(16))
            random_string = random_bytes.decode()
            self._worker_id = f'{self.server_name}_{random_string}'
        return self._worker_id

    async def initialize(self):
        self.server_task_queue_service = await aioredis.create_redis(**settings.SERVER_TASK_QUEUE)
        self.storage = aioelasticsearch.Elasticsearch(**settings.ES_STORAGE)

    async def get_input(self) -> typing.ByteString:
        try:
            k, v = await self.server_task_queue_service.brpop(self.server_name)
        except aioredis.errors.ConnectionForcedCloseError:
            if self.server_closing.done():
                logging.info('server task queue closed normally')
            else:
                logging.error('server task queue closed unexpectedly')
        else:
            return v

    def task_input(self):
        task: asyncio.Task = self.loop.create_task(self.get_input())
        task.set_name('input')
        return task

    def task_output(self):
        task = self.loop.create_task(self.result_q.get())
        task.set_name('output')
        return task

    async def handle_task_input(self, task_input: bytes):
        header_bytes, server, action, task_input_body = task_input.split(GameConsumer.PACK_DELIMITER)

        header_data: typing.Dict = dict(urllib.parse.parse_qsl(header_bytes))
        server_name = server.decode()
        assert self.server_name == server_name
        action_name = action.decode()

        task_input_dict: typing.Dict = self.parse_task_input(task_input_body)

        if action_name == 'create':
            await self.create_new_task_data(**task_input_dict)
        else:
            assert self.ID_NAME in task_input_dict

            task_id: typing.AnyStr = task_input_dict.get(self.ID_NAME)

            if task_id:
                task_instance = self.managed_tasks.get(task_id)
                if task_instance is None:
                    task_instance = await self.resume_task(task_id)

                if task_instance is None:
                    logging.error(f'task instance with {self.ID_NAME} = {task_id} cannot be found or created')
                else:
                    await task_instance.dispatch(action_name, task_input_dict)
            else:
                logging.error(f'no {self.ID_NAME} supplied')

    async def core_loop(self, task_data: typing.Dict, result_q: asyncio.Queue, output_q: asyncio.Queue):
        """for every task data create a task to run this coroutine"""
        pass

    async def create_new_task_data(self, **kwargs) -> typing.AnyStr:
        """return new created unique_id"""
        pass

    async def resume(self, unique_id):
        if unique_id in self.managed_tasks:
            return

        async with self.managed_task_change_lock:
            task_data: typing.Dict = await self.entity_get(unique_id=unique_id)
            task_instance = self.loop.create_task(self.core_loop(task_data=task_data))
            self.managed_tasks[unique_id] = task_instance

    @property
    def main_task_callables(self):
        if not self._main_task_callables:
            for item in dir(self):
                if item.startswith('task_'):
                    item_value = getattr(self, item)
                    if callable(item_value):
                        self._main_task_callables.append(item_value)
        return self._main_task_callables

    async def server_main(self):
        await self.initialize()
        self.server_started.set_result(True)
        self.main_tasks: typing.List[asyncio.Task] = [f() for f in self.main_task_callables]

        while not self.server_closing.done():
            await asyncio.wait(self.main_tasks, return_when=asyncio.FIRST_COMPLETED)

            if self.server_closing.done():
                continue

            for i, task in enumerate(self.main_tasks):
                if task.done():
                    task_name = task.get_name()
                    if task_name == 'input':
                        input_bytes: bytes = task.result()
                        print('get input', input_bytes)
                    elif task_name == 'output':
                        result: typing.Dict = task.result()
                        try:
                            group, content = self.result_getter(result)
                        except KeyError as e:
                            logging.error('key error', e)
                        else:
                            # send content by using do_send
                            await self.channel_layer.group_send(
                                group, {'type': 'do_send', 'content': content}
                            )
                    self.main_tasks[i] = self.main_task_callables[i]()

    async def start(self):
        logging.info('server starting ...')
        self.main_task = self.loop.create_task(self.server_main())
        await self.server_started
        logging.info('server started')
        await self.server_closed
        logging.info('server stopped')

    async def stop(self):
        logging.info('server stopping')
        self.server_closing.set_result(True)
        logging.info('releasing resources ...')
        await self.wait_stopped()
        logging.info('all resources released')
        self.server_closed.set_result(True)

    async def wait_stopped(self):
        logging.info('stop all managed tasks')
        async with self.managed_task_change_lock:
            for task_key in self.managed_tasks:
                task = self.managed_tasks[task_key]
                task.stop()
                await task.wait_stopped()
            self.managed_tasks.clear()

        logging.info('stop all main tasks')
        for task in self.main_tasks:
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass
        self.main_tasks.clear()

        logging.info('release message queue client')
        self.server_task_queue_service.close()
        await self.server_task_queue_service.wait_closed()

        logging.info('release storage client')
        await self.storage.close()






