import logging
import sys
import time
import uuid

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == "__main__":
    context = zmq.Context()
    responder = context.socket(zmq.REP)
    responder.connect("tcp://localhost:5560")

    name = uuid.uuid4().hex

    while True:
        request = responder.recv()
        logging.info("received request: %s", request)

        time.sleep(1)  # workload

        responder.send(f"response from {name}".encode())
