import logging
import os
import signal
import sys
import time

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    context = zmq.Context()
    socket = context.socket(zmq.ROUTER)
    socket.bind('tcp://*:5555')

    interrupted = False

    def callback(signum, stack):
        global interrupted
        interrupted = True

    signal.signal(signal.SIGINT, callback)
    signal.signal(signal.SIGTERM, callback)

    logging.info('PID is %s', os.getpid())

    poller = zmq.Poller()
    poller.register(socket, zmq.POLLIN)
    POLL_TIMEOUT = 3000

    while True:
        requesters = poller.poll(POLL_TIMEOUT)

        if requesters:
            addr = socket.recv()
            empty = socket.recv()
            message = socket.recv()
            logging.info('received request: %s', message)

            # do some work
            time.sleep(1)

            # send reply back to client
            socket.send(addr, zmq.SNDMORE)
            socket.send(b'', zmq.SNDMORE)
            socket.send(b'world')

        if interrupted:
            logging.info('breaking loop')
            break



