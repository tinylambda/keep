import logging
import queue
import random
import string
import time

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


def publish(q, n):
    choices = string.ascii_lowercase + string.digits

    for x in range(1, n + 1):
        host_id = "".join(random.choices(choices, k=4))
        instance_name = f"cattle-{host_id}"
        msg = PubSubMessage(message_id=x, instance_name=instance_name)
        # publish an item
        q.put(msg)
        logging.info(f"published {x} of {n} messages")
    q.put(None)


def consume(q):
    while True:
        # wait for an item from the publisher
        msg = q.get()

        # the publisher emits None to indicate that it is done
        if msg is None:
            break

        # process the message
        logging.info(f"consumed {msg}")
        # simulate I.O operation using sleep
        time.sleep(random.random())


def main():
    q = queue.Queue()
    publish(q, 5)
    consume(q)


if __name__ == "__main__":
    main()
