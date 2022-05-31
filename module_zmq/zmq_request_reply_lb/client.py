import logging
import sys

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == "__main__":
    context = zmq.Context()
    # socket talk to server
    requester = context.socket(zmq.REQ)
    requester.connect("tcp://localhost:5559")

    logging.info("start requesting")
    for i in range(10):
        logging.info("request %s", i)
        requester.send(b"hello")
        reply = requester.recv()
        logging.info("received reply %s", reply)
