import logging
import sys
import time

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    context = zmq.Context()
    publisher = context.socket(zmq.PUB)
    publisher.bind('tcp://*:5561')

    syncservice = context.socket(zmq.REP)
    syncservice.bind('tcp://*:5562')

    logging.info('waiting for subscribers')

    subscribers_connected = 0
    n_subscribers = 3
    while subscribers_connected < n_subscribers:
        msg = syncservice.recv()
        syncservice.send(b'')
        subscribers_connected += 1

    # wait for the last subscriber to be ready !
    time.sleep(1)

    logging.info('broadcasting messages')
    for _ in range(1000000):
        publisher.send(b'Rhubarb')
    publisher.send(b'END')
