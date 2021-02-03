import asyncio

tasks = []


async def handler():
    while True:
        print('Sleeping...')
        await asyncio.sleep(1)


async def dispatch():
    _loop = asyncio.get_event_loop()
    task = _loop.create_task(handler())
    tasks.append(task)
    task = _loop.create_task(handler())
    tasks.append(task)


async def wait_many_dispatch():
    await dispatch()


def canceller(task):
    task.cancel()


async def main():
    loop = asyncio.get_event_loop()
    await wait_many_dispatch()

    for t in tasks:
        print('cancelling')
        loop.call_soon(canceller, t)

    print(1)
    await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    print(2)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    # for t in tasks:
    #     print(t.result())

    # for t in tasks:
    #     t.cancel()

    async def test1():
        for t in tasks:
            try:
                await t
            except asyncio.CancelledError:
                print('here...')

    loop.run_until_complete(main())
    print('.....')

    loop.run_until_complete(test1())

    loop.close()

