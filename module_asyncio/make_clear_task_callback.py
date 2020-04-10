import asyncio


async def simple_task():
    while True:
        print(f'in simple task')
        await asyncio.sleep(2)

event_loop = asyncio.get_event_loop()
task = event_loop.create_task(simple_task())


async def dummy():
    await asyncio.sleep(10)
try:
    all_done = asyncio.Future()
    event_loop.run_forever()
finally:
    event_loop.close()
