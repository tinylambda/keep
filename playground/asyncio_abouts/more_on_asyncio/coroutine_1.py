import asyncio

from coroutines import f, g


async def main():
    result_f = await f()
    result_g = await g()
    print(result_f, result_g)


if __name__ == '__main__':
    asyncio.run(main())
