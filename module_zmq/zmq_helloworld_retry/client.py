import logging
import sys

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    context = zmq.Context()

    logging.info('connecting to zmq_helloworld server...')
    socket = context.socket(zmq.REQ)
    socket.connect('tcp://localhost:5555')

    poller = zmq.Poller()
    poller.register(socket, zmq.POLLIN)
    POLL_TIMEOUT = 3000

    for request in range(10):
        if not socket.closed:
            logging.info('sending request %s', request)
            socket.send(b'hello')

        readers = poller.poll(POLL_TIMEOUT)
        logging.info('readers: %s; socket closed?: %s', readers, socket.closed)
        if not readers:
            socket.close()
            poller.unregister(socket)

            logging.info('Reconnecting to zmq_helloworld server...')
            socket = context.socket(zmq.REQ)
            socket.connect('tcp://localhost:5555')

            poller.register(socket, zmq.POLLIN)
        else:
            # get the reply
            message = socket.recv()
            logging.info('received reply %s [%s]', request, message)
