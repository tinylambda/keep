import asyncio
import time


async def task():
    await asyncio.sleep(1)


async def main(i):
    tasks = [task() for _ in range(i)]

    inner_start = time.perf_counter()
    results = await asyncio.gather(*tasks)
    inner_end = time.perf_counter()
    inner_duration = inner_end - inner_start
    print("{:>8d}{:>16f}".format(i, inner_duration))


if __name__ == "__main__":
    for i in range(20):
        x = 2**i
        outer_start = time.perf_counter()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main(x))
        outer_end = time.perf_counter()
