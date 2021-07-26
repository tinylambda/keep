import asyncio

from coroutines import  f, g


async def main():
    coro_f = f()
    coro_g = g()

    result_f = await coro_f
    result_g = await coro_g

    print(result_f, result_g)


if __name__ == '__main__':
    asyncio.run(main())
