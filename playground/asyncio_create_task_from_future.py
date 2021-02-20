import asyncio


async def coro():
    future = asyncio.Future()
    task = asyncio.create_task(future)  # TypeError: a coroutine was expected, got <Future pending>
    await task


async def coro2():
    q = asyncio.Queue()
    task = loop.create_task(q.get())
    await task


async def coro3():
    task = loop.create_task(asyncio.sleep(2))
    await task


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(coro3())

