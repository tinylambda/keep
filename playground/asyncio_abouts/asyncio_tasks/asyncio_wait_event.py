import asyncio
import logging
import random
import sys

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


async def set_event(event, delay=3):
    logging.info("waiting for event for %s seconds", delay)
    await asyncio.sleep(delay)
    event.set()


async def shutdown(loop):
    tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
    [task.cancel() for task in tasks]
    await asyncio.gather(*tasks, return_exceptions=True)
    loop.stop()


async def long_running_worker(stop_event: asyncio.Event):
    i = 0
    while True and not stop_event.is_set():
        logging.info("process task %s", i)
        await asyncio.sleep(random.random())
        i += 1

    logging.info("Done")
    loop = asyncio.get_running_loop()
    loop.create_task(shutdown(loop))


def main():
    loop = asyncio.get_event_loop()
    stop_event = asyncio.Event()
    loop.create_task(set_event(stop_event, 10))
    loop.create_task(long_running_worker(stop_event))
    loop.run_forever()


if __name__ == "__main__":
    main()
