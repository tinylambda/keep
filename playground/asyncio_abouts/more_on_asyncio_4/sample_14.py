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
        self.hostname = f'{self.instance_name}.example.net'


async def publish(queue):
    choices = string.ascii_lowercase + string.digits

    while True:
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
        logging.info(f'consumed {msg}')
        asyncio.create_task(handle_message(msg))


def main():
    queue = asyncio.Queue()
    loop = asyncio.get_event_loop()

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
