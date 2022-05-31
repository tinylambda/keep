import logging
import random
import sys
import threading
import time

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


def worker_task():
    _context = zmq.Context()
    worker = _context.socket(zmq.DEALER)
    worker.connect("tcp://localhost:5671")

    while True:
        # empty frame and ready message
        worker.send(b"", zmq.SNDMORE)
        worker.send(b"Hi Boss")

        # empty frame
        worker.recv()
        workload = worker.recv()
        logging.info(
            "%s, get workload from server: %s",
            threading.current_thread().name,
            workload,
        )


if __name__ == "__main__":
    NBR_WORKERS = 10

    context = zmq.Context()
    broker = context.socket(zmq.ROUTER)
    broker.bind("tcp://*:5671")

    for _ in range(NBR_WORKERS):
        threading.Thread(target=worker_task).start()

    end_time = time.time() + 5
    workers_fired = 0

    while True:
        identity = broker.recv()
        broker.recv()
        broker.recv()

        # just send to dealer
        broker.send(identity, zmq.SNDMORE)
        broker.send(b"", zmq.SNDMORE)
        broker.send(f"server: hello {identity}, {random.random()}".encode())
        time.sleep(0.5)
