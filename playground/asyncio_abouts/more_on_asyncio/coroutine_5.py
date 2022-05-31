import asyncio

import async_timeout

from coroutines import f, g_sleep


async def main():
    async with async_timeout.timeout(5.0):
        await f()
        await g_sleep(10)


if __name__ == "__main__":
    asyncio.run(main())
