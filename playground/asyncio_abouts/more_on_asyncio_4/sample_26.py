import asyncio
import logging
import random
import signal
import string
import time
import uuid

import attr

logging.basicConfig(
    level=logging.INFO,
    format="{asctime},{msecs} {levelname}: {message}",
    style="{",
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


class RestartedFailed(Exception):
    pass


async def publish(q: asyncio.Queue):
    choices = string.ascii_lowercase + string.digits

    while True:
        msg_id = str(uuid.uuid4())
        host_id = "".join(random.choices(choices, k=4))
        instance_name = f"cattle-{host_id}"
        msg = PubSubMessage(message_id=msg_id, instance_name=instance_name)
        logging.debug(f"published message {msg}")
        asyncio.create_task(q.put(msg))
        await asyncio.sleep(random.random())


async def restart_host(msg: PubSubMessage):
    await asyncio.sleep(random.random())

    if random.randrange(1, 5) == 3:
        raise RestartedFailed(f"could not restart {msg.hostname}")
    msg.restarted = True
    logging.info(f"restarted {msg}")


async def save(msg: PubSubMessage):
    # await asyncio.sleep(random.random())  # <-------- NOTE
    time.sleep(1 + random.random())

    if random.randrange(1, 5) == 3:
        raise Exception(f"could not save {msg}")

    msg.saved = True
    logging.info(f"saved {msg} into database")


async def extend(msg: PubSubMessage, event: asyncio.Event):
    while not event.is_set():
        msg.extended_cnt += 1
        logging.info(f"extended deadline by 3 seconds for {msg}")
        await asyncio.sleep(2)


async def cleanup(msg: PubSubMessage, event: asyncio.Event):
    await event.wait()
    await asyncio.sleep(random.random())
    msg.acked = True
    logging.info(f"done. acked {msg}")


def handle_results(results, msg: PubSubMessage):
    for result in results:
        if isinstance(result, RestartedFailed):
            logging.error(f"retrying for failure to restart: {msg.hostname}")
        elif isinstance(result, Exception):
            logging.error(f"handling general error : {result}")


async def handle_message(msg: PubSubMessage):
    event = asyncio.Event()

    asyncio.create_task(extend(msg, event))
    asyncio.create_task(cleanup(msg, event))

    # remove return_exceptions=True for debugging purpose
    results = await asyncio.gather(save(msg), restart_host(msg))
    handle_results(results, msg)
    event.set()


async def consume(q: asyncio.Queue):
    while True:
        msg: PubSubMessage = await q.get()
        logging.info(f"pulled {msg}")
        asyncio.create_task(handle_message(msg))


async def shutdown(loop, sig=None):
    if sig:
        logging.info(f"received exit signal {sig.name}")
    logging.info("closing database connections")
    logging.info("nacking outstanding messages")
    tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]

    [task.cancel() for task in tasks]

    logging.info("cancelling outstanding tasks")
    await asyncio.gather(*tasks, return_exceptions=True)
    logging.info(f"flushing metrics")
    loop.stop()


async def monitor_tasks():
    while True:
        tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
        [t.print_stack(limit=5) for t in tasks]
        await asyncio.sleep(2)


def main():
    loop = asyncio.get_event_loop()
    loop.set_debug(True)  # or you can use the commandline at the bottom to enable debug
    # loop.slow_callback_duration = 2.5  # in seconds, how long is treated as slow

    signals = (signal.SIGHUP, signal.SIGTERM, signal.SIGINT)
    for s in signals:
        loop.add_signal_handler(
            s, lambda s=s: asyncio.create_task(shutdown(loop, sig=s))
        )

    # remove loop.set_exception_handler for debugging purpose
    q = asyncio.Queue()

    try:
        loop.create_task(publish(q))
        loop.create_task(consume(q))
        loop.run_forever()
    finally:
        loop.close()
        logging.info("successfully shutdown the Mayhem service.")


if __name__ == "__main__":
    main()

# PYTHONASYNCIODEBUG=1 python playground/asyncio_abouts/more_on_asyncio_4/sample_26.py
