import asyncio
import inspect
import json
import logging
import typing

import aioredis


SERVER_TASK_QUEUE = {
    'address': 'redis://localhost',
    'db': 14,
    'password': 'rpassword',
}


class Task:
    def __init__(self, result_q: asyncio.Queue):
        self.loop = asyncio.get_event_loop()

        self.result_q: asyncio.Queue = result_q
        self.input_q: asyncio.Queue = asyncio.Queue()

        self.task_started: asyncio.Future = asyncio.Future()
        self.task_closing: asyncio.Future = asyncio.Future()
        self.task_closed :asyncio.Future = asyncio.Future()

        self.__tick_tasks: typing.List[asyncio.Task] = []
        self.__main_task: asyncio.Task = None

        self.default_interval: float = 1.0

    async def tick_check(self):
        while True:
            print('in tick check')
            await asyncio.sleep(self.default_interval)

    async def tick_update(self):
        while True:
            print('in tick update')
            await asyncio.sleep(self.default_interval)

    async def tick_main(self):
        while True:
            print('in tick main')
            await asyncio.sleep(self.default_interval)

    async def call(self, arg: dict):
        await self.input_q.put(arg)

    async def task_input(self):
        task = self.loop.create_task(self.input_q.get())
        task.set_name('input')
        return task

    async def main(self):
        print('in main')
        while True:
            print('waiting user input')
            user_input: typing.Dict = await self.input_q.get()
            action = user_input.get('action')
            if action:
                user_input.pop('action')
            action_method = getattr(self, f'action_{action}')
            if action_method:
                result = await action_method(user_input)
                print('result is ', result)

    async def start(self):
        print('starting task')
        print('start all tick tasks')

        self.task_started.set_result(True)
        for item in dir(self):
            if item.startswith('tick_'):
                item_value = getattr(self, item)
                print(inspect.isfunction(item_value))
                if callable(item_value):
                    __task = self.loop.create_task(item_value())
                    self.__tick_tasks.append(__task)
        print('start main task')
        self.__main_task = self.loop.create_task(self.main())

    async def stop(self):
        self.task_closing.set_result(True)
        for t in self.__tick_tasks:
            t.cancel()
            try:
                await t
            except asyncio.CancelledError:
                pass

        self.__main_task.cancel()
        try:
            await self.__main_task
        except asyncio.CancelledError:
            pass
        self.task_closed.set_result(True)


class Server:
    def __init__(self):
        self.server_started: asyncio.Future = asyncio.Future()
        self.server_closing: asyncio.Future = asyncio.Future()
        self.server_closed: asyncio.Future = asyncio.Future()

        self.loop = asyncio.get_event_loop()
        self.task_q_service = None
        self.default_interval: float = 1.0

        self.tick_task: asyncio.Task = None
        self.main_task: asyncio.Task = None

    @property
    def server_name(self):
        return self.__class__.__name__

    async def initialize(self):
        self.task_q_service = await aioredis.create_redis(**SERVER_TASK_QUEUE)

    async def server_tick(self):
        while True:
            print('in server tick')
            await asyncio.sleep(self.default_interval)

    async def get_q_input(self):
        try:
            k, v = await self.task_q_service.brpop(self.server_name)
        except aioredis.errors.ConnectionForcedCloseError:
            if self.server_closing.done():
                logging.info('server task queue closed normally')
            else:
                logging.error('server task queue closed unexpectedly')
        else:
            return v

    def task_input(self):
        task = self.loop.create_task(self.get_q_input())
        task.set_name('input')
        return task

    async def server_main(self):
        task_callables = [self.task_input]
        tasks = [f() for f in task_callables]
        self.server_started.set_result(True)
        while not self.server_closing.done():
            print('waiting input at q service', self.server_name)
            await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

            if self.server_closing.done():
                print('server closing set, continue')
                continue

            for i, task in enumerate(tasks):
                if task.done():
                    task_name = task.get_name()
                    if task_name == 'input':
                        result_bytes: bytes = task.result()
                        result_dict: typing.Dict = json.loads(result_bytes)
                        print('get input: ', result_dict)
                    tasks[i] = task_callables[i]()

    async def start(self):
        print('initialize server')
        await self.initialize()
        self.tick_task = self.loop.create_task(self.server_tick())
        self.main_task = self.loop.create_task(self.server_main())
        await self.server_started
        print('server started')
        await self.server_closed
        print('server closed')

    async def stop(self):
        print('stopping server')
        self.server_closing.set_result(True)
        self.tick_task.cancel()
        try:
            await self.tick_task
        except asyncio.CancelledError:
            pass

        self.main_task.cancel()
        try:
            await self.main_task
        except asyncio.CancelledError:
            pass

        self.server_closed.set_result(True)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    server = Server()
    loop.run_until_complete(server.start())











