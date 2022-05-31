import logging
import sys

import numpy.random
import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


def sync(bind_to: str):
    # use bind socket + 1
    parts = bind_to.split(":")
    pre = ":".join(parts[:-1])
    port = int(parts[-1]) + 1
    sync_with = f"{pre}:{port}"
    ctx = zmq.Context.instance()
    s = ctx.socket(zmq.REP)
    s.bind(sync_with)
    logging.info("waiting for subscriber to connect...")
    s.recv()
    logging.info("done.")
    s.send(b"go")


if __name__ == "__main__":
    array_count = 10
    array_size = 5
    context = zmq.Context()
    publisher = context.socket(zmq.PUB)
    bind_to = "tcp://*:5555"
    publisher.bind(bind_to)
    sync(bind_to)

    logging.info("sending arrays")
    for i in range(array_count):
        a = numpy.random.rand(array_size, array_size)
        publisher.send_pyobj(a)
    logging.info("done.")
