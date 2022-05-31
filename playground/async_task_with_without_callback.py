import asyncio


async def task1():
    print("in task1")
    await asyncio.sleep(10)
    print("done task1")


async def task2():
    print("in task2")
    await asyncio.sleep(10)
    print("done task2")


async def run1():
    loop = asyncio.get_event_loop()
    task = loop.create_task(task1())
    loop.call_soon(task.cancel)
    task.add_done_callback(lambda f: print("callback: task1 done"))
    result = await task
    return result


async def run2():
    loop = asyncio.get_event_loop()
    task = loop.create_task(task2())
    loop.call_soon(task.cancel)
    try:
        result = await task
    except asyncio.CancelledError:
        print("run2 canceled task")
        result = None
    return result


def main():
    loop = asyncio.get_event_loop()
    coro = run2()
    loop.run_until_complete(coro)


if __name__ == "__main__":
    main()
