import logging
import sys

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

"""
1. start two publish servers:
# python server.py py 5555
# python server.py go 5556

2. start this reader
python reader.py
"""

if __name__ == "__main__":
    context = zmq.Context()

    py_reader = context.socket(zmq.SUB)
    py_reader.connect("tcp://localhost:5555")
    py_reader.setsockopt(zmq.SUBSCRIBE, b"")

    go_reader = context.socket(zmq.SUB)
    go_reader.connect("tcp://localhost:5556")
    go_reader.setsockopt(zmq.SUBSCRIBE, b"")

    while True:
        try:
            py_message = py_reader.recv(zmq.DONTWAIT)
            logging.info("processing py message: %s", py_message)
        except zmq.error.Again:
            pass
        try:
            go_message = go_reader.recv(zmq.DONTWAIT)
            logging.info("processing go message: %s", go_message)
        except zmq.error.Again:
            pass
