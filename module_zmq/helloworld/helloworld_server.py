import logging
import sys
import time

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind('tpc://*:5555')

    while True:
        # wait for next request from client
        message = socket.recv()
        logging.info('received request: %s', message)

        # do some work
        time.sleep(1)

        # send reply back to client
        socket.send(b'world')
