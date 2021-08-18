import asyncio
import logging
import random
import signal
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
    await asyncio.sleep(random.random())
    msg.restart = True
    logging.info(f"Restarted {msg.hostname}")


async def save(msg):
    await asyncio.sleep(random.random())
    msg.save = True
    logging.info(f"Saved {msg} into database")


async def cleanup(msg, event):
    # this will block the rest of the coroutine until event.set is called
    await event.wait()
    # unhelpful simulation of I/O work
    await asyncio.sleep(random.random())
    msg.acked = True
    logging.info(f"Done. Acked {msg}")


async def extend(msg, event):
    while not event.is_set():
        msg.extended_cnt += 1
        logging.info(f"Extended deadline by 3 seconds for {msg}")
        await asyncio.sleep(2)


async def handle_message(msg):
    event = asyncio.Event()
    asyncio.create_task(extend(msg, event))
    asyncio.create_task(cleanup(msg, event))

    await asyncio.gather(save(msg), restart_host(msg))
    event.set()


async def consume(queue):
    while True:
        msg = await queue.get()
        logging.info(f"Consumed {msg}")
        asyncio.create_task(handle_message(msg))


async def shutdown(signal, loop):
    logging.info(f"Received exit signal {signal.name}...")
    logging.info("Closing database connections")
    logging.info("Nacking outstanding messages")
    tasks = [t for t in asyncio.all_tasks() if t is not
             asyncio.current_task()]

    [task.cancel() for task in tasks]

    logging.info(f"Cancelling {len(tasks)} outstanding tasks")
    await asyncio.gather(*tasks, return_exceptions=True)
    logging.info(f"Flushing metrics")
    loop.stop()


def main():
    loop = asyncio.get_event_loop()
    signals = (signal.SIGHUP, signal.SIGTERM, signal.SIGINT)
    for s in signals:
        loop.add_signal_handler(
            s, lambda s=s: asyncio.create_task(shutdown(s, loop)))
    queue = asyncio.Queue()

    try:
        loop.create_task(publish(queue))
        loop.create_task(consume(queue))
        loop.run_forever()
    finally:
        loop.close()
        logging.info("Successfully shutdown the Mayhem service.")


if __name__ == "__main__":
    main()
