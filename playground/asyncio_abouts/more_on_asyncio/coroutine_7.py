import asyncio

from coroutines import f, g_sleep


async def main():
    task_f = asyncio.create_task(f())
    task_g = asyncio.create_task(g_sleep(1))
    done, pending = await asyncio.wait([task_f, task_g])

    for t in done:
        try:
            if t is task_f:
                print(f"the result of f() is {await task_f}")
        except Exception as e:
            print(f"f() failed with {repr(e)}")


if __name__ == "__main__":
    asyncio.run(main())
