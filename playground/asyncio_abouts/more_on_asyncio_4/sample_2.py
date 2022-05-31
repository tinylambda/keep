import asyncio
import logging
import random
import string

import attr

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s,%(msecs)d %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)


@attr.s
class PubSubMessage:
    instance_name = attr.ib()
    message_id = attr.ib(repr=False)
    hostname = attr.ib(repr=False, init=False)

    def __attrs_post_init__(self):
        self.hostname = f"{self.instance_name}.example.net"


async def publish(queue, n):
    choices = string.ascii_lowercase + string.digits

    for x in range(1, n + 1):
        host_id = "".join(random.choices(choices, k=4))
        instance_name = f"cattle-{host_id}"
        msg = PubSubMessage(message_id=x, instance_name=instance_name)
        await queue.put(msg)
        logging.info(f"published {x} of {n} messages")
    await queue.put(None)


async def consume(queue):
    while True:
        # wait for an item from the publisher
        msg = await queue.get()
        if msg is None:
            break
        # process the msg
        logging.info(f"consumed {msg}")
        # unhelpful simulation of i/o work
        await asyncio.sleep(random.random())


def main():
    """not a service"""
    queue = asyncio.Queue()
    asyncio.run(publish(queue, 5))
    asyncio.run(consume(queue))


def main_old():
    queue = asyncio.Queue()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(publish(queue, 5))
    loop.run_until_complete(consume(queue))
    loop.close()
    logging.info("successfully shutdown the service")


def main2():
    """cannot close the loop gracefully"""
    queue = asyncio.Queue()
    loop = asyncio.get_event_loop()
    loop.create_task(publish(queue, 5))
    loop.create_task(consume(queue))
    loop.run_forever()
    loop.close()
    logging.info(f"successfully shutdown the Mayhem service.")


def main3():
    """
    finally close the loop
    """
    queue = asyncio.Queue()
    loop = asyncio.get_event_loop()
    try:
        loop.create_task(publish(queue, 5))
        loop.create_task(consume(queue))
        loop.run_forever()
    except KeyboardInterrupt:
        logging.info("process interrupted")
    finally:
        loop.close()
        logging.info(f"successfully shutdown the Mayhem service.")


if __name__ == "__main__":
    # main()
    # main_old()
    main2()
    # main3()
