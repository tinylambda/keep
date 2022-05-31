import asyncio


async def f():
    return 1


async def g():
    return 2


async def g_ex():
    raise RuntimeError("go")


async def g_sleep(n):
    await asyncio.sleep(n)
    return 2
