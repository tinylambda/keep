import logging
import sys

import attr
import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    context = zmq.Context()

    logging.info('connecting to helloworld server...')
    socket = context.socket(zmq.REQ)
    socket.connect('tcp://localhost:5555')

    for request in range(10):
        logging.info('sending request %s', request)
        socket.send(b'hello')

        # get the reply
        message = socket.recv()
        logging.info('received reply %s [%s]', request, message)
