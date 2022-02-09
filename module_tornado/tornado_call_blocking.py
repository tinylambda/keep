import asyncio
import functools
import time

import tornado.gen
from tornado.ioloop import IOLoop


async def call_blocking():
    print('start blocking in executor')
    await IOLoop.current().run_in_executor(None, time.sleep, 10)
    print('end blocking in executor')


async def normal_task():
    for i in range(20):
        print('Normal task running')
        await tornado.gen.sleep(1)
    print('Normal task done')


if __name__ == '__main__':
    loop = IOLoop.current()
    loop.add_future(asyncio.ensure_future(call_blocking()), lambda f: print(f.result()))

    def normal_cb(f, use_loop: IOLoop):
        print(f.result())
        use_loop.stop()

    loop.add_future(asyncio.ensure_future(normal_task()), callback=functools.partial(normal_cb, use_loop=loop))
    loop.start()

