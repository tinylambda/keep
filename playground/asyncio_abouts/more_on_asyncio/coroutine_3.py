import asyncio

from coroutines import f, g


async def main():
    task_f = asyncio.create_task(f())
    task_g = asyncio.create_task(g())

    await asyncio.sleep(0.1)
    result_f = await task_f
    result_g = await task_g

    print(result_f, result_g)


if __name__ == '__main__':
    asyncio.run(main())
