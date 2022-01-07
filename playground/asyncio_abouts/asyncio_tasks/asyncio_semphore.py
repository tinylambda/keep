import asyncio
import logging
import random
import sys

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


async def fetch_sem(n):
    sem = asyncio.Semaphore(n)
    for _ in range(n):
        await sem.acquire()
    return sem


async def sem_release(sem: asyncio.Semaphore, times=3):
    for _ in range(times):
        logging.info('release sem...')
        await asyncio.sleep(1)
        sem.release()


async def sem_trigger(sem: asyncio.Semaphore, event: asyncio.Event, n):
    ack_num = 0
    while True:
        await sem.acquire()
        ack_num += 1
        if ack_num == n:
            event.set()


async def full_worker():
    loop = asyncio.get_event_loop()
    sig_event = asyncio.Event()
    sem: asyncio.Semaphore = await fetch_sem(10)
    logging.info('%s', sem.locked)
    logging.info('wait to trigger ...')
    loop.create_task(sem_trigger(sem, sig_event, 10))
    loop.create_task(sem_release(sem, 10))

    await sig_event.wait()
    logging.info('I can start work now!')
    await asyncio.sleep(random.random())
    logging.info('Bye!')


if __name__ == '__main__':
    asyncio.run(full_worker())
