import logging
import random
import sys
import threading
import time
import uuid

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


def client_task():
    context = zmq.Context()
    client = context.socket(zmq.DEALER)
    identity = f'CLIENT_{uuid.uuid4().hex}'
    client.setsockopt(zmq.IDENTITY, identity.encode())
    client.connect('tcp://localhost:5570')

    poller = zmq.Poller()
    poller.register(client, zmq.POLLIN)

    request_nbr = 0
    message = f'{identity} request {request_nbr}'.encode()
    logging.info('sending: %s', message)
    client.send(message)

    need_break: bool = random.random() < 0.5

    while True:
        poller.poll()
        msg = client.recv()
        if need_break:
            logging.info('client_task %s: break', identity)
            break
        logging.info('%s: get message %s', identity, msg)


def server_worker(context: zmq.Context):
    worker = context.socket(zmq.DEALER)
    worker.connect('inproc://backend')

    while True:
        # The DEALER socket gives us the reply envelope and message
        identity = worker.recv()
        content = worker.recv()

        logging.info('server_worker => identity: %s, content: %s', identity, content)
        replies = random.randint(0, 10)
        logging.info('send %s replies to %s', replies, identity)
        for _ in range(replies):
            time.sleep(1)
            worker.send(identity, zmq.SNDMORE)
            worker.send(content)


def server_task():
    context = zmq.Context()

    # frontend tasks to clients over tcp
    frontend = context.socket(zmq.ROUTER)
    frontend.bind('tcp://*:5570')

    # backend talks to workers over inproc
    backend = context.socket(zmq.DEALER)
    backend.bind('inproc://backend')

    # launch pool of worker threads, precise number is not critical
    thread_nbr = 0
    for _ in range(5):
        threading.Thread(target=server_worker, args=(context, ), daemon=True).start()
        thread_nbr += 1
    logging.info('%s server_task started', thread_nbr)

    zmq.proxy(frontend, backend)


if __name__ == '__main__':
    threading.Thread(target=client_task, daemon=True).start()
    threading.Thread(target=client_task, daemon=True).start()
    threading.Thread(target=client_task, daemon=True).start()

    threading.Thread(target=server_task, daemon=True).start()

    time.sleep(10)
    logging.info('done')
