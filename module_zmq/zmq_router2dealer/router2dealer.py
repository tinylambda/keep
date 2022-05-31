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

    total = 0
    while True:
        # empty frame and ready message
        worker.send(b"", zmq.SNDMORE)
        worker.send(b"Hi Boss")

        # empty frame
        worker.recv()
        workload = worker.recv()
        finished = workload == b"Fired!"
        if finished:
            logging.info("Completed %s tasks", total)
            break
        total += 1
        # do some work
        time.sleep(random.random())


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

        broker.send(identity, zmq.SNDMORE)
        broker.recv()  # empty frame
        broker.recv()  # worker's response
        broker.send(b"", zmq.SNDMORE)

        if time.time() < end_time:
            broker.send(b"Work harder")
        else:
            broker.send(b"Fired!")
            workers_fired += 1
            if workers_fired == NBR_WORKERS:
                break
