import asyncio
import functools
import time


async def simple_coro():
    await asyncio.sleep(2)
    print('simple coro done')


async def main_coro():
    i = 0
    while True:
        print(f'main coro: {i}')
        await asyncio.sleep(1)
        i += 1


def sync_metric(i):
    print('sync metric', i)
    time.sleep(4)
    return 'OK'


def main():
    loop = asyncio.new_event_loop()
    print(id(loop), id(asyncio.get_event_loop()))
    asyncio.set_event_loop(loop)
    print(id(loop), id(asyncio.get_event_loop()))
    loop.create_task(main_coro())
    simple_task = loop.create_task(simple_coro())
    simple_task.add_done_callback(functools.partial(sync_metric))
    loop.run_forever()


if __name__ == '__main__':
    main()

