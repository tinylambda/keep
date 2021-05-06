import time
import trio


async def double_sleep(x):
    await trio.sleep(2 * x)


if __name__ == '__main__':
    print(time.time())
    trio.run(double_sleep, 3)
    print(time.time())

