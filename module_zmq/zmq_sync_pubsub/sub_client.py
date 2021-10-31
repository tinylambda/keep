import logging
import sys
import time

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    context = zmq.Context()
    subscriber = context.socket(zmq.SUB)
    subscriber.connect('tcp://localhost:5561')
    subscriber.setsockopt(zmq.SUBSCRIBE, b'')

    # connect and send sync request
    syncclient = context.socket(zmq.REQ)
    syncclient.connect('tcp://localhost:5562')
    syncclient.send(b'')

    # wait for sync reply
    msg = syncclient.recv()

    msg_received = 0
    while True:
        msg = subscriber.recv()
        if b'END' == msg:
            break
        msg_received += 1

    logging.info('received %s updates', msg_received)
