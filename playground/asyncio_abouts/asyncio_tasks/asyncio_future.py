import asyncio
import logging

logging.basicConfig(level=logging.INFO)


async def cost_long_time(s: int):
    await asyncio.sleep(s)
    logging.info("done")


async def raise_exception():
    raise RuntimeError("just for example")


async def do():
    # task = asyncio.create_task(cost_long_time(10))
    # logging.info('result: %s', task.result())

    task = asyncio.create_task(raise_exception())
    logging.info("result: %s", task.result())


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(do())
    loop.close()
    logging.info("main done")


if __name__ == "__main__":
    main()
