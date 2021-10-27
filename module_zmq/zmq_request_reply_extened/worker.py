import logging
import sys
import time

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    context = zmq.Context()
    responder = context.socket(zmq.REP)
    responder.connect('tcp://localhost:5560')

    while True:
        request = responder.recv()
        logging.info('received request: %s', request)

        time.sleep(1)  # workload

        responder.send(b'world')
