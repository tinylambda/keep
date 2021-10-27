import logging
import sys

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    context = zmq.Context()

    reader = context.socket(zmq.SUB)
    reader.connect('tcp://localhost:8100')
    reader.setsockopt(zmq.SUBSCRIBE, b'')

    logging.info('reading from lb proxy')
    while True:
        message = reader.recv()
        logging.info('processing message: %s', message)
