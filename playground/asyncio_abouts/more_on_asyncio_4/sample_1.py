import asyncio, datetime


async def hello():
    print(f'[{datetime.datetime.now()}] Hello...')
    await asyncio.sleep(1)  # some I/O intensive work
    print(f'[{datetime.datetime.now()}] ...World!')


if __name__ == '__main__':
    asyncio.run(hello())
