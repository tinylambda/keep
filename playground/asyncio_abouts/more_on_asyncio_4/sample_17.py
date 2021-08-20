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
        self.hostname = f'{self.instance_name}.example.net'


async def publish(queue):
    choices = string.ascii_lowercase + string.digits

    while True:
        logging.info('publishing...')
        msg_id = str(uuid.uuid4())
        host_id = ''.join(random.choices(choices, k=4))
        instance_name = f'cattle-{host_id}'
        msg = PubSubMessage(message_id=msg_id, instance_name=instance_name)
        # publish an item
        asyncio.create_task(queue.put(msg))
        logging.debug(f'published message {msg}')
        # simulate randomness of publishing messages
        await asyncio.sleep(random.random())


async def restart_host(msg: PubSubMessage):
    # unhelpful simulation of I/O work
    await asyncio.sleep(random.random())
    msg.restarted = True
    logging.info(f'restarted {msg.hostname}')


async def save(msg: PubSubMessage):
    # unhelpful simulation of I/O work
    await asyncio.sleep(random.random())
    msg.saved = True
    logging.info(f'saved {msg} into database')


async def cleanup(msg: PubSubMessage, event: asyncio.Event):
    # this will block the rest of the coroutine until event.set is called
    await event.wait()
    # unhelpful simulation of I/O work
    await asyncio.sleep(random.random())
    msg.acked = True
    logging.info(f'done. acked {msg}')


async def extend(msg: PubSubMessage, event: asyncio.Event):
    while not event.is_set():
        msg.extended_cnt += 1
        logging.info(f'extended deadline by 3 seconds for {msg}')
        # want to sleep for less than the deadline amount
        await asyncio.sleep(2)


async def handle_message(msg: PubSubMessage):
    event = asyncio.Event()
    asyncio.create_task(extend(msg, event))
    asyncio.create_task(cleanup(msg, event))
    await asyncio.gather(save(msg), restart_host(msg))
    event.set()


async def consume(queue: asyncio.Queue):
    while True:
        msg = await queue.get()
        # totally realistic exception
        if random.randrange(1, 5) == 3:
            raise Exception(f'could not consume {msg}')

        logging.info(f'consumed {msg}')
        asyncio.create_task(handle_message(msg))


async def shutdown(loop, sig=None):
    """cleanup tasks tied to the service's shutdown"""
    if sig:
        logging.info(f'received exit signal {sig.name}')
    logging.info('closing database connections')
    logging.info('nacking outstanding messages')
    tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
    [task.cancel() for task in tasks]
    logging.info(f'cancelling {len(tasks)} outstanding tasks')
    await asyncio.gather(*tasks, return_exceptions=True)
    logging.info('flushing metrics')
    loop.stop()


def handle_exception(loop, context):
    # context['message'] will always be there; but context['exception'] may not
    msg = context.get('exception', context['message'])
    logging.error(f'caught exception: {msg}')
    logging.info('shutting down...')
    asyncio.create_task(shutdown(loop))


def main():
    queue = asyncio.Queue()
    loop = asyncio.get_event_loop()
    # may want to catch other signals too
    signals = (signal.SIGHUP, signal.SIGTERM, signal.SIGINT)
    for s in signals:
        loop.add_signal_handler(s, lambda s=s: asyncio.create_task(shutdown(loop, s)))

    loop.set_exception_handler(handle_exception)

    try:
        loop.create_task(publish(queue))
        loop.create_task(consume(queue))
        loop.run_forever()
    except KeyboardInterrupt:
        logging.info('process interrupted')
    finally:
        loop.close()
        logging.info('successfully shutdown the Mayhem service.')


if __name__ == '__main__':
    main()
