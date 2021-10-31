import logging
import sys
import threading

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


def step1(context: zmq.Context):
    xmitter = context.socket(zmq.PAIR)
    xmitter.connect('inproc://step2')
    logging.info('step1 ready, signaling step2')
    xmitter.send(b'READY')


def step2(context: zmq.Context):
    receiver = context.socket(zmq.PAIR)
    receiver.bind('inproc://step2')
    threading.Thread(target=step1, args=(context, ), daemon=True).start()

    # step1 completed will signal step2
    msg = receiver.recv()

    # connect to step3, tell it step2 completed
    xmitter = context.socket(zmq.PAIR)
    xmitter.connect('inproc://step3')
    logging.info('step2 ready, signaling step3')
    xmitter.send(b'READY')


if __name__ == '__main__':
    context = zmq.Context()
    receiver = context.socket(zmq.PAIR)
    receiver.bind('inproc://step3')
    threading.Thread(target=step2, args=(context, ), daemon=True).start()

    msg = receiver.recv()
    logging.info('step3 done')
    logging.info('test successful')
