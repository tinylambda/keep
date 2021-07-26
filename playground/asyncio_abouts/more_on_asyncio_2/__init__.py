import asyncio
import time


JOB_DURATION = 0.01
JOB_COUNT = 200


async def heartbeat():
    while True:
        start = time.time()
        await asyncio.sleep(1)
        delay = time.time() - start - 1
        print(f'heartbeat delay = {delay:.3f}s')


async def process():
    time.sleep(JOB_DURATION)


async def main():
    asyncio.create_task(heartbeat())
    await asyncio.sleep(2.5)
    print('begin processing')
    count = JOB_COUNT
    for _ in range(JOB_COUNT):
        asyncio.create_task(process())
    await asyncio.sleep(5)


WORKER_COUNT = 4


async def main_with_semaphore():
    asyncio.create_task(heartbeat())
    await asyncio.sleep(2.5)
    sem = asyncio.Semaphore(WORKER_COUNT)

    async def process():
        await sem.acquire()
        time.sleep(JOB_DURATION)
        sem.release()

    print('begin processing')
    for _ in range(JOB_COUNT):
        asyncio.create_task(process())

    await asyncio.sleep(5)


async def main_with_queue():
    asyncio.create_task(heartbeat())
    await asyncio.sleep(2.5)

    queue = asyncio.Queue(maxsize=1)  # change to 2 to see what happens

    async def worker():
        while True:
            coro = await queue.get()
            await coro
            queue.task_done()

    workers = [asyncio.create_task(worker()) for _ in range(WORKER_COUNT)]
    print('begin processing')
    for _ in range(JOB_COUNT):
        await queue.put(process())
        await asyncio.sleep(0)
    await queue.join()
    print('end processing')

    for w in workers:
        w.cancel()

    await asyncio.sleep(2)


async def producer_consumer():
    queue = asyncio.Queue()
    done = asyncio.Condition()

    async def producer():
        for i in range(100_000):
            await queue.put(i)
            await asyncio.sleep(0)
        await queue.join()
        async with done:
            done.notify()

    async def consumer():
        while True:
            await queue.get()
            print(f'qsize = {queue.qsize()}')
            queue.task_done()
            await asyncio.sleep(0)
            await asyncio.sleep(0)

    asyncio.create_task(producer())
    asyncio.create_task(consumer())

    async with done:
        await done.wait()


if __name__ == '__main__':
    # asyncio.run(main_with_queue())
    asyncio.run(producer_consumer())
