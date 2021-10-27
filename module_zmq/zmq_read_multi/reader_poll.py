import logging
import sys

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    context = zmq.Context()

    py_reader = context.socket(zmq.SUB)
    py_reader.connect('tcp://localhost:5555')
    py_reader.setsockopt(zmq.SUBSCRIBE, b'')

    go_reader = context.socket(zmq.SUB)
    go_reader.connect('tcp://localhost:5556')
    go_reader.setsockopt(zmq.SUBSCRIBE, b'')

    poller = zmq.Poller()
    poller.register(py_reader, zmq.POLLIN)
    poller.register(go_reader, zmq.POLLIN)

    while True:
        readers = poller.poll()
        logging.info('ready %s', len(readers))
        for reader, item in readers:
            message = reader.recv()
            if reader == py_reader:
                logging.info('py[%s]: %s', item, message)
            elif reader == go_reader:
                logging.info('go[%s]: %s', item, message)
