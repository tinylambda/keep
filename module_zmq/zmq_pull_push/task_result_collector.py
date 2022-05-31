import logging
import sys
import time

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == "__main__":
    receiver_bind_to = "tcp://*:5558"
    context = zmq.Context()
    receiver = context.socket(zmq.PULL)
    receiver.bind(receiver_bind_to)

    controller = context.socket(zmq.PUB)
    controller.bind("tcp://*:5559")

    # wait for start of batch
    start_signal = receiver.recv()
    logging.info("receive start signal %s", start_signal)

    # start our clock
    start_time = time.perf_counter()
    task_nbr = 100

    for i in range(task_nbr):
        message = receiver.recv()
        if i == task_nbr - 1:
            logging.info(":")
        else:
            logging.info(".")

    logging.info(
        "total elapsed time: %s msec", (time.perf_counter() - start_time) * 1000
    )

    logging.info("notify all workers to quit")
    controller.send(b"kill")
