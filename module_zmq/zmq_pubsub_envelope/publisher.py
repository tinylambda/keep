import logging
import sys

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    context = zmq.Context()
    publisher = context.socket(zmq.PUB)
    publisher.bind('tcp://*:5563')

    while True:
        publisher.send(b'A', zmq.SNDMORE)
        publisher.send(b'we do not want to see this')

        publisher.send(b'B', zmq.SNDMORE)
        publisher.send(b'we would like to see this')
