import logging
import random
import sys
import time

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == "__main__":
    sender_bind_to = "tcp://*:5557"
    context = zmq.Context()
    sender = context.socket(zmq.PUSH)
    sender.bind(sender_bind_to)

    sink_address = "tcp://localhost:5558"
    sink = context.socket(zmq.PUSH)
    sink.connect(sink_address)
    input("press enter when the workers are ready: ")
    logging.info("sending tasks to workers ...")

    # the first message is '0' and signals start of batch
    sink.send(b"0")

    # send 100 tasks
    task_nbr = 100
    total_msec = 0

    for i in range(task_nbr):
        workload = random.randint(0, 100) + 1
        total_msec += workload
        sender.send(f"{workload}".encode())

    logging.info("total expected cost: %d msec", total_msec)
    time.sleep(1)  # give zmq time to deliver
