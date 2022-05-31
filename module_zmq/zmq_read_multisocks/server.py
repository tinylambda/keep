import datetime
import logging
import random
import sys
import time

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == "__main__":
    name = sys.argv[1]
    port = sys.argv[2]
    logging.info("%s %s", name, port)

    context = zmq.Context()
    publisher = context.socket(zmq.PUB)

    bind_to = f"tcp://*:{port}"
    publisher.bind(bind_to)

    while True:
        ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        publisher.send(f"{name}-{port}: {ts}".encode("utf-8"))
        time.sleep(random.random())

# python server.py py 5555
# python server.py go 5556
