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
        logging.info("release sem...")
        await asyncio.sleep(1)
        sem.release()


async def sem_trigger(sem: asyncio.Semaphore, event: asyncio.Event, n):
    while n > 0:
        await sem.acquire()
        n -= 1
    event.set()


async def full_worker():
    loop = asyncio.get_event_loop()
    sig_event = asyncio.Event()
    n = 5
    sem: asyncio.Semaphore = await fetch_sem(n)
    logging.info("%s", sem.locked())
    logging.info("wait to trigger ...")
    loop.create_task(sem_trigger(sem, sig_event, n))
    loop.create_task(sem_release(sem, n))

    await sig_event.wait()
    logging.info("I can start work now!")
    await asyncio.sleep(random.random())
    logging.info("Bye!")


if __name__ == "__main__":
    asyncio.run(full_worker())
