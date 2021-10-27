import logging
import sys

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

"""
start a pub server on port 5556
# python module_zmq/zmq_read_multisocks/server.py x 5556

start normal subscribers
# python module_zmq/zmq_read_multisocks/reader_poll.py

start a subscriber connected to 8100
# python module_zmq/zmq_pubsub_lb/reader_from_proxy.py
"""

if __name__ == '__main__':
    context = zmq.Context()
    frontend = context.socket(zmq.XSUB)
    frontend.connect('tcp://localhost:5556')

    backend = context.socket(zmq.XPUB)
    backend.bind('tcp://*:8100')

    logging.info('constructing proxy')
    zmq.proxy(frontend, backend)
