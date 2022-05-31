# https://stackoverflow.com/questions/34753401/difference-between-coroutine-and-future-task-in-python-3-5

import asyncio
import time


async def p(word):
    print(f"{time.time()} - {word}")


async def main():
    loop = asyncio.get_event_loop()
    coro = p("await")
    task2 = loop.create_task(p("create_task"))
    await coro
    await task2


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
