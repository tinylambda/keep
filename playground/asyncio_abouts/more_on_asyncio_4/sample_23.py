import asyncio
import concurrent.futures
import functools
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


def consume_sync(q, loop):
    while True:
        # wait for an item from the publisher
        msg = q.get()
        # process the message
        logging.info(f"consumed {msg}")
        loop.create_task(handle_message(msg))
        # substitute for handling a message
        time.sleep(random.random())


async def publish(executor, q):
    logging.info("starting publisher")
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(executor, publish_sync, q)


async def consume(executor, q):
    logging.info("starting consumer")
    loop = asyncio.get_running_loop()
    asyncio.ensure_future(
        loop.run_in_executor(executor, consume_sync, q, loop), loop=loop
    )


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


def handle_exception(executor, loop, context):
    msg = context.get("exception", context["message"])
    logging.error(f"caught exception: {msg}")
    logging.info("shutting down")
    asyncio.create_task(shutdown(loop, executor))


async def restart_host(msg: PubSubMessage):
    # unhelpful simulation of I/O work
    await asyncio.sleep(random.random())
    # totally realistic exception
    # if random.randrange(1, 5) == 3:
    #     raise RestartFailed(f'could not restart {msg.hostname}')
    msg.restarted = True
    logging.info(f"restarted {msg.hostname}")


async def save(msg: PubSubMessage):
    # unhelpful simulation of I/O work
    await asyncio.sleep(random.random())
    # totally realistic exception
    # if random.randrange(1, 5) == 3:
    #     raise Exception(f'could not save {msg}')
    msg.saved = True
    logging.info(f"saved {msg} into database")


async def cleanup(msg: PubSubMessage, event: asyncio.Event):
    # this will block the rest of the coroutine until event.set is called
    await event.wait()
    # unhelpful simulation of I/O work
    await asyncio.sleep(random.random())
    msg.acked = True
    logging.info(f"done. acked {msg}")


async def extend(msg: PubSubMessage, event: asyncio.Event):
    while not event.is_set():
        msg.extended_cnt += 1
        logging.info(f"extended deadline by 3 seconds for {msg}")
        # want to sleep for less than the deadline amount
        await asyncio.sleep(2)


def handle_results(results, msg):
    for result in results:
        if isinstance(result, RestartFailed):
            logging.error(f"retrying for failure to restart: {msg.hostname}")
        elif isinstance(result, Exception):
            logging.error(f"handling general error {result}")


async def handle_message(msg: PubSubMessage):
    event = asyncio.Event()
    loop = asyncio.get_running_loop()
    loop.create_task(extend(msg, event))
    loop.create_task(cleanup(msg, event))
    results = await asyncio.gather(
        save(msg), restart_host(msg), return_exceptions=True, loop=loop
    )
    handle_results(results, msg)
    event.set()


def main():
    executor = concurrent.futures.ThreadPoolExecutor()
    loop = asyncio.get_event_loop()
    signals = (signal.SIGHUP, signal.SIGINT, signal.SIGTERM)
    for s in signals:
        loop.add_signal_handler(
            s, lambda s=s: asyncio.create_task(shutdown(loop, executor, sig=s))
        )
    handle_exception_func = functools.partial(handle_exception, executor)
    loop.set_exception_handler(handle_exception_func)
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
