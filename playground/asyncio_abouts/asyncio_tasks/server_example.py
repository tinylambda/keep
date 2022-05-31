import asyncio
import binascii
import os
import typing

from channels.layers import get_channel_layer


class HandlerTask:
    def __init__(self):
        self.managed_tasks: typing.Dict[typing.AnyStr, asyncio.Task] = {}
        self.task_change_lock = asyncio.Lock()


class ServerExample:
    MIN_TICK_INTERVAL = 1.0

    def __init__(self):
        self.loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()

        self.managed_tasks: typing.Dict[typing.AnyStr, asyncio.Task] = {}
        self.managed_task_change_lock = asyncio.Lock()
        self.last_tick_time = self.loop.time()

        self.server_closing: asyncio.Future = asyncio.Future()
        self.server_closed: asyncio.Future = asyncio.Future()

        self._all_tick_callables: typing.List[typing.Callable] = []
        self._all_server_callables: typing.List[typing.Callable] = []

        self._worker_id: typing.AnyStr = None
        self.server_main_task: asyncio.Task = None
        self.server_tick_task: asyncio.Task = None

    @property
    def worker_id(self):
        if not self._worker_id:
            random_bytes = os.urandom(16)
            random_string = random_bytes.decode()
            self._worker_id = f"{self.__class__.__name__}_{random_string}"
        return self._worker_id

    @property
    def all_tick_callables(self):
        if not self._all_tick_callables:
            for item in dir(self):
                if item.startswith("tick_"):
                    item_value = getattr(self, item)
                    if callable(item_value):
                        self._all_tick_callables.append(item_value)
        return self._all_tick_callables

    async def tick_shrink_managed_tasks(self):
        async with self.managed_task_change_lock:
            await asyncio.sleep(1)

    async def attach_task(self, task_id: typing.AnyStr, task: asyncio.Task):
        async with self.managed_task_change_lock:
            pass

    async def detach_task(self, task_id: typing.AnyStr):
        async with self.managed_task_change_lock:
            pass

    async def server_tick(self):
        while not self.server_closing.done():
            self.last_tick_time = self.loop.time()

            tick_tasks = [self.loop.create_task(f()) for f in self.all_tick_callables]

            tick_tasks_start = self.loop.time()
            await asyncio.wait(tick_tasks, return_when=asyncio.ALL_COMPLETED)
            tick_tasks_cost = self.loop.time() - tick_tasks_start

            next_wait = max(self.MIN_TICK_INTERVAL, tick_tasks_cost)
            await asyncio.sleep(next_wait)

    async def server_main(self):
        while not self.server_closing.done():
            await asyncio.sleep(0.5)

    def start(self):
        self.server_main_task = self.loop.create_task(self.server_main())
        self.server_tick_task = self.loop.create_task(self.server_tick())

    def stop(self):
        self.server_closing.set_result(True)

    async def wait_finished(self):
        await asyncio.sleep(5)  # cleanup
        self.server_closed.set_result(True)


if __name__ == "__main__":

    async def run_server():
        server = ServerExample()
        server.start()
        await server.server_closed

    # async def stop_server():
    #     await server.stop()

    # try:
    asyncio.run(run_server())
    # except KeyboardInterrupt:
    #     pass
    #     # print('stopping server')
    #     # asyncio.run(stop_server())
    #     # print('server stopped')
