import asyncio
import logging
import random
import string
import uuid

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
    restarted = attr.ib(repr=False, default=False)
    saved = attr.ib(repr=False, default=False)
    acked = attr.ib(repr=False, default=False)
    extended_cnt = attr.ib(repr=False, default=0)

    def __attrs_post_init__(self):
        self.hostname = f"{self.instance_name}.example.net"


async def cleanup(msg):
    # unhelpful simulation of I/O work
    await asyncio.sleep(random.random())
    msg.acked = True
    logging.info(f"Done. Acked {msg}")


async def handle_message(msg):
    event = asyncio.Event()
    # this task will block on event and yield control to the loop
    asyncio.create_task(extend(msg, event))
    await asyncio.gather(save(msg), restart_host(msg))
    event.set()


async def publish(queue):
    choices = string.ascii_lowercase + string.digits

    while True:
        msg_id = str(uuid.uuid4())
        host_id = "".join(random.choices(choices, k=4))
        instance_name = f"cattle-{host_id}"
        msg = PubSubMessage(message_id=msg_id, instance_name=instance_name)
        asyncio.create_task(queue.put(msg))
        logging.debug(f"Published message {msg}")
        await asyncio.sleep(random.random())


async def restart_host(msg):
    # unhelpful simulation of I/O work
    await asyncio.sleep(random.random())
    msg.restarted = True
    logging.info(f"Restarted {msg.hostname}")


async def extend(msg: PubSubMessage, event: asyncio.Event):
    while not event.is_set():
        msg.extended_cnt += 1
        logging.info(f"extended deadline by 3 seconds for {msg}")
        await asyncio.sleep(2)
    else:
        await cleanup(msg)


async def save(msg):
    await asyncio.sleep(random.random())
    msg.saved = True
    logging.info(f"Saved {msg} into database")


async def consume(queue):
    while True:
        msg = await queue.get()
        logging.info(f"Consumed {msg}")
        asyncio.create_task(handle_message(msg))


def main():
    queue = asyncio.Queue()
    loop = asyncio.get_event_loop()

    try:
        loop.create_task(publish(queue))
        loop.create_task(consume(queue))
        loop.run_forever()
    except KeyboardInterrupt:
        logging.info("Process interrupted")
    finally:
        loop.close()
        logging.info("Successfully shutdown the Mayhem service.")


if __name__ == "__main__":
    main()
