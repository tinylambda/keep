import asyncio


async def task(name):
    print("in task", name)
    await asyncio.sleep(1)


async def main():
    coros = []
    for i in range(3):
        coros.append(task(i))

    for coro in coros:
        await coro


async def main2():
    loop = asyncio.get_event_loop()
    tasks = []
    for i in range(3):
        _task = loop.create_task(task(i))
        tasks.append(_task)

    await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
