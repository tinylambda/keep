import  asyncio


async def t():
    print('hello world')

async def main():
    loop = asyncio.get_event_loop()
    task = loop.create_task(t())
    print(task.done())
    await asyncio.sleep(1)
    print(task.done())
    print('main done')


asyncio.run(main())