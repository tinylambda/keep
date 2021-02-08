import asyncio


async def t(i):
    while True:
        print(f'in task {i}...')
        await asyncio.sleep(1)


async def main():
    _loop = asyncio.get_event_loop()
    initial_tasks = [loop.create_task(t(i)) for i in range(3)]
    while True:
        print(dir(initial_tasks[0]))
        await asyncio.wait(initial_tasks, return_when=asyncio.FIRST_COMPLETED)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
