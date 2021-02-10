import asyncio
import itertools


class RoleLoop:
    def __init__(self, role_id, input_q, output_q):
        self.role_id = role_id
        self.input_q = input_q
        self.output_q = output_q

        self.running_tasks = []
        self.new_tasks = []

        self.loop = asyncio.get_event_loop()
        self.new_task_lock = asyncio.Lock()

    async def add_task(self, task):
        async with self.new_task_lock:
            self.new_tasks.append(task)


class GameServer:
    def __init__(self):
        self.role_loops = []
        self.running_tasks = []
        self.new_tasks = []
        self.new_task_lock = asyncio.Lock()

        self.loop = asyncio.get_event_loop()
        self.stopped = False
        self.stop_future = asyncio.Future()
        self.loop_result_q = asyncio.Queue()

    async def initialize(self):
        return True

    async def start(self):
        print('init game server')
        await self.initialize()

        await asyncio.sleep(10)
        print('init done')

    async def stop(self):
        print('stop game server')
        for task in itertools.chain(self.new_tasks, self.running_tasks):
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass
        print('stop done')

    async def common_task(self, waiters=[]):
        pass

    async def run_server(self):
        task = self.loop.create_task(self.start())
        await self.add_task(task)
        async with self.new_task_lock:
            self.running_tasks.extend(self.new_tasks)
            self.new_tasks.clear()

        while not self.stopped:
            pass

    async def stop_server(self):
        pass

    async def add_task(self, task):
        async with self.new_task_lock:
            if not self.stopped:
                self.new_tasks.append(task)


if __name__ == '__main__':
    gs = GameServer()
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(gs.run_server())
    except KeyboardInterrupt:
        loop.run_until_complete(gs.stop())

