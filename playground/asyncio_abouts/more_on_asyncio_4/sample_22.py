import asyncio
import concurrent.futures
import logging
import queue
import random
import signal
import string
import time
import uuid

import attr

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s,%(msecs)s %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)


@attr.s
class PubSubMessage:
    instance_name = attr.ib()
    message_id = attr.ib(repr=False)
    hostname = attr.ib(repr=False, init=False)

    def __attrs_post_init__(self):
        self.hostname = f"{self.instance_name}.example.net"


def publish_sync(q):
    choices = string.ascii_lowercase + string.digits

    while True:
        msg_id = str(uuid.uuid4())
        host_id = "".join(random.choices(choices, k=4))
        instance_name = f"cattle-{host_id}"
        msg = PubSubMessage(message_id=msg_id, instance_name=instance_name)
        # publish an item
        q.put(msg)
        logging.info(f"published {msg}")
        # simulate randomness of publishing messages
        time.sleep(random.random())


def consume_sync(q):
    while True:
        # wait for an item from the publisher
        msg = q.get()
        # process the message
        logging.info(f"consumed {msg}")
        # substitute for handling a message
        time.sleep(random.random())


async def publish(executor, q):
    logging.info("starting publisher")
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(executor, publish_sync, q)


async def consume(executor, q):
    logging.info("starting consumer")
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(executor, consume_sync, q)


async def shutdown(loop, executor, sig=None):
    """cleanup tasks tied to the service's shutdown."""
    if sig:
        logging.info(f"received exit signal {sig.name}")
    logging.info("closing database connections")
    logging.info("nacking outstanding messages")
    tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
    [task.cancel() for task in tasks]

    logging.info(f"cancelling {len(tasks)} outstanding tasks")
    await asyncio.gather(*tasks, return_exceptions=True)

    logging.info("shutting down executor")
    executor.shutdown(wait=False)

    logging.info(f"releasing {len(executor._threads)} threads from executor")
    for thread in executor._threads:
        try:
            thread._tstate_lock.release()
        except Exception:
            pass

    logging.info("flushing metrics")
    loop.stop()


def main():
    executor = concurrent.futures.ThreadPoolExecutor()
    loop = asyncio.get_event_loop()
    signals = (signal.SIGHUP, signal.SIGINT, signal.SIGTERM)
    for s in signals:
        loop.add_signal_handler(
            s, lambda s=s: asyncio.create_task(shutdown(loop, executor, sig=s))
        )
    q = queue.Queue()

    try:
        loop.create_task(publish(executor, q))
        loop.create_task(consume(executor, q))
        loop.run_forever()
    finally:
        loop.close()
        logging.info("successfully shutdown the Mayhem service.")


if __name__ == "__main__":
    main()
