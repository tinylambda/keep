import asyncio
import random

s = 0


async def add(use_lock):
    # async with use_lock:
    await asyncio.sleep(random.random())  # Simulate different I/O delays
    global s
    tmp = s + 1
    await asyncio.sleep(0)  # Yield control to the event loop
    s = tmp


async def main(use_lock):
    tasks = [add(use_lock) for _ in range(10000)]
    await asyncio.gather(
        *tasks
    )

event_loop = asyncio.get_event_loop()
try:
    lock = asyncio.Lock()
    event_loop.run_until_complete(main(lock))
    print(s)
finally:
    event_loop.close()

