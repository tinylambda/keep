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


class RestartFailed(Exception):
    pass


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
        logging.debug(f"published message {msg}")
        await asyncio.sleep(random.random())


async def restart_host(msg: PubSubMessage):
    await asyncio.sleep(random.random())
    if random.randrange(1, 5) == 3:
        raise RestartFailed(f"could not restart {msg.hostname}")
    msg.restarted = True
    logging.info(f"restarted {msg.hostname}")


async def save(msg: PubSubMessage):
    await asyncio.sleep(random.random())
    if random.randrange(1, 5) == 3:
        raise Exception(f"Could not save {msg}")
    msg.saved = True
    logging.info(f"saved {msg} into database")


async def cleanup(msg: PubSubMessage, event: asyncio.Event):
    await event.wait()
    msg.acked = True
    logging.info(f"done, acked {msg}")


async def extend(msg: PubSubMessage, event: asyncio.Event):
    while not event.is_set():
        msg.extended_cnt += 1
        logging.info(f"extended deadline by 3 seconds for {msg}")
        await asyncio.sleep(2)


async def handle_message(msg: PubSubMessage):
    event = asyncio.Event()
    asyncio.create_task(extend(msg, event))
    asyncio.create_task(cleanup(msg, event))
    # the first raised exception is immediately propagated to the task that awaits on gather()
    await asyncio.gather(save(msg), restart_host(msg))
    event.set()


async def consume(queue):
    while True:
        msg = await queue.get()
        # if random.randrange(1, 5) == 3:
        #     raise Exception(f"could not consume {msg}")
        logging.info(f"consumed {msg}")
        asyncio.create_task(handle_message(msg))


async def shutdown(loop, signal=None):
    if signal:
        logging.info(f"received exit signal {signal.name}")
    logging.info("closing database connections")
    logging.info("nacking outstanding messages")
    tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
    [task.cancel() for task in tasks]
    logging.info(f"cancelling {len(tasks)} outstanding tasks")
    await asyncio.gather(*tasks, return_exceptions=True)
    logging.info("flushing metrics")
    loop.stop()


def handle_exception(loop, context):
    msg = context.get("exception", context["message"])
    logging.error(f"caught exception {msg}")
    logging.info("shutting down...")
    asyncio.create_task(shutdown(loop))


def main():
    loop = asyncio.get_event_loop()
    signals = (signal.SIGHUP, signal.SIGTERM, signal.SIGINT)
    for s in signals:
        loop.add_signal_handler(s, lambda s=s: asyncio.create_task(shutdown(s, loop)))
    loop.set_exception_handler(handle_exception)

    queue = asyncio.Queue()
    try:
        loop.create_task(consume(queue))
        loop.create_task(publish(queue))
        loop.run_forever()
    finally:
        loop.close()
        logging.info("successfully shutdown the service")


if __name__ == "__main__":
    main()
