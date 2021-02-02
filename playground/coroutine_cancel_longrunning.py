import asyncio


async def get_result():
    return 100


async def handler(message):
    while True:
        print('sleeping')
        await asyncio.sleep(.5)


async def main():
    task = asyncio.create_task(handler(111))
    await task


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

