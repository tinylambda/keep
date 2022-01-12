import logging
import sys

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    context = zmq.Context()

    logging.info('connecting to zmq_helloworld server...')
    socket = context.socket(zmq.DEALER)
    socket.setsockopt(zmq.SNDHWM, 10)
    socket.connect('tcp://localhost:5555')

    socket2 = context.socket(zmq.DEALER)
    socket2.setsockopt(zmq.SNDHWM, 10)
    socket2.connect('tcp://localhost:7777')

    for request in range(20):
        msg = f'hello1-{request}'.encode()
        logging.info('sending message: %s', msg)
        socket.send(msg)

    for request in range(20):
        msg = f'hello2-{request}'.encode()
        logging.info('sending message: %s', msg)
        socket2.send(msg)

    poller = zmq.Poller()
    poller.register(socket, zmq.POLLIN)
    poller.register(socket2, zmq.POLLIN)

    while True:
        socks = poller.poll()
        logging.info(socks)
        for sock, mask in socks:
            logging.info('received1: %s', sock.recv())
            logging.info('received2: %s', sock.recv())
