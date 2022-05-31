import logging
import queue
import sys
import threading
import time

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


def client_task():
    context = zmq.Context()
    client = context.socket(zmq.REQ)
    client.setsockopt(zmq.IDENTITY, f"CLIENT_{time.time()}".encode())
    client.connect("ipc://frontend.ipc")
    client.send(b"HELLO")

    reply = client.recv()
    logging.info("Client: %s", reply)


def worker_task():
    context = zmq.Context()
    worker = context.socket(zmq.REQ)
    worker.setsockopt(zmq.IDENTITY, f"WORKER_{time.time()}".encode())
    worker.connect("ipc://backend.ipc")
    worker.send(b"READY")

    while True:
        identity = worker.recv()
        empty = worker.recv()
        request = worker.recv()

        logging.info("Worker: %s", request)
        worker.send(identity, zmq.SNDMORE)
        worker.send(empty, zmq.SNDMORE)
        worker.send(b"OK")


if __name__ == "__main__":
    CLIENT_NBR = 10
    WORKER_NBR = 3

    use_context = zmq.Context()
    frontend = use_context.socket(zmq.ROUTER)
    backend = use_context.socket(zmq.ROUTER)

    frontend.bind("ipc://frontend.ipc")
    backend.bind("ipc://backend.ipc")

    client_nbr = 0
    for _ in range(CLIENT_NBR):
        threading.Thread(target=client_task, daemon=False).start()
        client_nbr += 1

    worker_nbr = 0
    for _ in range(WORKER_NBR):
        threading.Thread(target=worker_task, daemon=True).start()
        worker_nbr += 1

    available_workers = 0
    workers_queue = queue.Queue()

    while True:
        poller = zmq.Poller()
        poller.register(backend, zmq.POLLIN)
        poller.register(frontend, zmq.POLLIN)

        # Poll frontend only if we have available workers
        socks = poller.poll()
        have_worker = False
        have_client = False
        for sock, mask in socks:
            if backend == sock:
                have_worker = True
            if frontend == sock:
                have_client = True

        if not have_worker:
            logging.info("no worker ready, break")
            break

        # Handle worker activity on backend
        if have_worker:
            # Queue worker identity for load-balancing
            worker_id = backend.recv()
            assert available_workers < WORKER_NBR
            workers_queue.put_nowait(worker_id)

            # Second frame is empty
            empty = backend.recv()

            # Third frame is READY or else a client reply identity
            client_id = backend.recv()
            # If client reply, send rest back to frontend
            if b"READY" != client_id:
                empty = backend.recv()

                reply = backend.recv()
                frontend.send(client_id, zmq.SNDMORE)
                frontend.send(b"", zmq.SNDMORE)
                frontend.send(reply)

                client_nbr -= 1
                if client_nbr == 0:
                    break

            if have_client:
                # Now get next client request, route to last-used worker
                # Client request is [identity][empty][request]
                client_id = frontend.recv()
                empty = frontend.recv()
                request = frontend.recv()

                backend.send(workers_queue.get_nowait(), zmq.SNDMORE)
                backend.send(b"", zmq.SNDMORE)
                backend.send(client_id, zmq.SNDMORE)
                backend.send(b"", zmq.SNDMORE)
                backend.send(request)

                available_workers -= 1
