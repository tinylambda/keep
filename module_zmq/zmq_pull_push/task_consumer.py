import logging
import sys
import time

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    context = zmq.Context()

    # socket to receive messages on
    receiver = context.socket(zmq.PULL)
    receiver.connect('tcp://localhost:5557')

    # socket to send messages to
    sender = context.socket(zmq.PUSH)
    sender.connect('tcp://localhost:5558')

    while True:
        message = receiver.recv()
        logging.info('received message %s', message)
        workload = int(message.decode())
        time.sleep(workload / 1000.)

        sender.send(b'')
