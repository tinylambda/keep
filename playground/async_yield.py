import asyncio


async def test_coro():
    for i in range(10):
        await asyncio.sleep(1)
        yield i


async def run_coro():
    async for item in test_coro():
        print('getting item', item)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_coro())


if __name__ == '__main__':
    main()

