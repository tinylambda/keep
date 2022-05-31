import asyncio
import random


async def simple_task(name):
    print("in task", name)
    randint = random.randint(4, 8)
    await asyncio.sleep(randint)
    raise RuntimeError(f"Error in task {name}")


async def main():
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(simple_task(f"task_{i}")) for i in range(5)]
    await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    for task in tasks:
        if task.done():
            print(task.result())

        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    # loop.close()
