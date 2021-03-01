import asyncio
import binascii
import json
import logging
import os
import typing
import urllib.parse

import aioelasticsearch
import aioredis

from channels.layers import get_channel_layer
from django.conf import settings

from ..consumers import GameConsumer


class ServerBase:
    ID_NAME = 'id'
    SERVER_TASK_CLASS = None

    def __init__(self, min_tick_interval=1.0):
        self.server_name = self.__class__.__name__
        self.min_tick_interval = min_tick_interval

        self.managed_tasks: typing.Dict[typing.AnyStr, asyncio.Task] = {}
        self.managed_task_change_lock: asyncio.Lock = asyncio.Lock()

        self.loop = asyncio.get_event_loop()
        self.channel_layer = get_channel_layer()

        self.server_task_queue = None
        self.server_storage = None

        self.server_closing = asyncio.Future()
        self.server_closed = asyncio.Future()

        self._worker_id = None

    @property
    def worker_id(self):
        if not self._worker_id:
            random_bytes = binascii.hexlify(os.urandom(16))
            random_string = random_bytes.decode()
            self._worker_id = f'{self.server_name}_{random_string}'
        return self._worker_id

    async def initialize(self):
        self.server_task_queue = await aioredis.create_redis(**settings.SERVER_TASK_QUEUE)
        self.server_storage = aioelasticsearch.Elasticsearch(**settings.ES_STORAGE)

    async def get_input(self) -> typing.ByteString:
        try:
            k, v = await self.server_task_queue.brpop(self.server_name)
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

    async def output(self, group_name: typing.AnyStr, result: typing.ByteString):
        await self.channel_layer.group_send(group_name, {
            'type': 'do_send',
            'result': result,
        })

    @classmethod
    def parse_task_input(cls, task_input: bytes):
        return json.loads(task_input)

    async def create_task(self, task_args: typing.Dict):
        pass

    async def resume_task(self, task_id: typing.AnyStr):
        pass

    async def handle(self, task_input: bytes):
        extra_bytes, server, action, task_input_body = task_input.split(GameConsumer.PACK_DELIMITER)

        extra_data: typing.Dict = dict(urllib.parse.parse_qsl(extra_bytes))
        server_name = server.decode()
        assert self.server_name == server_name
        action_name = action.decode()

        task_input_dict: typing.Dict = self.parse_task_input(task_input_body)

        if action_name == 'setup':
            task_instance = self.SERVER_TASK_CLASS(extra_data, task_input_dict)
        else:
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


