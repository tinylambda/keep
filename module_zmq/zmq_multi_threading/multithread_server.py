import logging
import sys
import threading

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


def worker_routine(context: zmq.Context):
    receiver = context.socket(zmq.REP)
    receiver.connect("inproc://workers")

    while True:
        msg = receiver.recv()
        logging.info("received: %s", msg)
        receiver.send(f"{threading.current_thread().name}: world".encode())


if __name__ == "__main__":
    ctx = zmq.Context()  # zeromq context is thread safe

    # for the clients
    clients = ctx.socket(zmq.ROUTER)
    clients.bind("tcp://*:5555")

    # for the workers
    workers = ctx.socket(zmq.DEALER)
    workers.bind("inproc://workers")

    n_threads = 5
    for i in range(n_threads):
        threading.Thread(target=worker_routine, args=(ctx,), daemon=True).start()

    zmq.proxy(clients, workers)
