import logging
import sys

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    context = zmq.Context()

    logging.info('connecting to zmq_helloworld server...')
    socket = context.socket(zmq.DEALER)
    socket.connect('tcp://localhost:5555')

    for request in range(20):
        msg = f'hello-{request}'.encode()
        logging.info('sending message: %s', msg)
        socket.send(msg)

    while True:
        msg = socket.recv()
        logging.info('msg: %s', msg)
