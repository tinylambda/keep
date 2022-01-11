import logging
import random
import sys

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    context = zmq.Context()

    logging.info('connecting to zmq_helloworld server...')
    socket = context.socket(zmq.REQ)
    socket.connect('tcp://localhost:5555')

    send_message = f'hello-{random.randint(0, 1000)}'.encode()

    for request in range(10):
        logging.info('sending request %s', send_message)
        socket.send(send_message)

        # get the reply
        received_message = socket.recv()
        logging.info('received reply %s [%s]', request, received_message)
