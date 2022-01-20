import logging
import os
import random
import signal
import sys
import time

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    context = zmq.Context()
    context.setsockopt(zmq.LINGER, 10 * 1000)
    print(dir(context))
    print(context._sockets)
    socket = context.socket(zmq.REP)
    socket.bind('tcp://*:5555')

    interrupted = False

    def callback(signum, stack):
        global interrupted
        interrupted = True

    signal.signal(signal.SIGINT, callback)
    signal.signal(signal.SIGTERM, callback)

    logging.info('PID is %s', os.getpid())

    while True:
        # wait for next request from client
        print(context._sockets)
        message = socket.recv()
        logging.info('received request: %s', message)

        # do some work
        time.sleep(random.randint(4, 7))

        if interrupted:
            logging.info('breaking loop')
            break

        # send reply to client
        socket.send(b'your message is ' + message)

