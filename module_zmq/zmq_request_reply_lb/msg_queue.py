import logging
import sys

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    context = zmq.Context()
    frontend = context.socket(zmq.ROUTER)
    frontend.bind('tcp://*:5559')

    backend = context.socket(zmq.DEALER)
    backend.bind('tcp://*:5560')

    logging.info('proxy constructing')
    zmq.proxy(frontend, backend)
