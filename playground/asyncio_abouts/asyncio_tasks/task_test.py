import asyncio


async def t(i):
    print('hello world')
    await asyncio.sleep(i)
    raise RuntimeError(f'exception {i}')


async def main():
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(t(i)) for i in range(5)]

    while True:
        await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        for task in tasks:
            if task.done():
                if task.exception():
                    print(task.exception())
                else:
                    print(task.result())
        tasks = [item for item in tasks if not item.done()]
        if len(tasks) == 0:
            break

    print('main done')


asyncio.run(main())

