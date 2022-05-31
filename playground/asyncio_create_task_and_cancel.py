import asyncio

tasks = []


async def handler():
    while True:
        print("Sleeping...")
        await asyncio.sleep(1)


async def dispatch():
    _loop = asyncio.get_event_loop()
    task = loop.create_task(handler())
    tasks.append(task)
    task = loop.create_task(handler())
    tasks.append(task)


async def wait_many_dispatch():
    await dispatch()


def canceller(task):
    task.cancel()


async def main():
    loop = asyncio.get_event_loop()
    await wait_many_dispatch()

    for t in tasks:
        print("cancelling")
        loop.call_soon(canceller, t)

    for t in tasks:
        await t

    await asyncio.sleep(2)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(wait_many_dispatch())

    # for t in tasks:
    #     t.cancel()

    async def test1():
        for t in tasks:
            t.cancel()

        for t in tasks:
            try:
                await t
            except asyncio.CancelledError:
                print("here")
                pass

    loop.run_until_complete(test1())
    loop.close()
