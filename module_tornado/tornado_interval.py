import asyncio
import random
import time

from tornado import gen
from tornado.ioloop import IOLoop


async def minute_loop():
    print('Start ticking')
    while True:
        nxt = gen.sleep(10)
        await gen.sleep(random.randint(1, 5))
        await nxt
        print('GO', time.asctime())


async def minute_loop2():
    print('Start ticking')
    while True:
        nxt = asyncio.ensure_future(asyncio.sleep(10))  # Start in the background
        await asyncio.sleep(random.randint(1, 5))
        await nxt
        print('GO', time.asctime())


if __name__ == '__main__':
    loop = IOLoop.current()
    loop.spawn_callback(minute_loop)
    # loop.spawn_callback(minute_loop2)
    loop.start()
