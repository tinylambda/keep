import logging
import random
import sys
import threading
import time
import uuid

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


def tick_task():
    context = zmq.Context()
    publisher = context.socket(zmq.PUB)
    publisher.bind('tcp://*:7777')

    while True:
        publisher.send(b'K')
        publisher.send(b'V')
        time.sleep(1)


def client_task():
    context = zmq.Context()
    tick_source = context.socket(zmq.SUB)
    tick_source.connect('tcp://localhost:7777')
    tick_source.setsockopt(zmq.SUBSCRIBE, b'')

    client = context.socket(zmq.DEALER)
    identity = f'CLIENT_{uuid.uuid4().hex}'
    client.setsockopt(zmq.IDENTITY, identity.encode())
    client.connect('tcp://localhost:5570')

    poller = zmq.Poller()

    poller.register(tick_source, zmq.POLLIN)
    poller.register(client, zmq.POLLIN)

    request_nbr = 0
    while True:
        socks = poller.poll()
        for sock, mask in socks:
            if sock is tick_source:
                message = f'{identity} request {request_nbr}'.encode()
                logging.info('sending: %s', message)
                tick_source.recv()
                tick_source.recv()
                client.send(message)
                request_nbr += 1
            else:
                msg = client.recv()
                logging.info('%s: get message %s', identity, msg)


def server_worker(context: zmq.Context):
    worker = context.socket(zmq.DEALER)
    worker.connect('inproc://backend')

    while True:
        # The DEALER socket gives us the reply envelope and message
        identity = worker.recv()
        content = worker.recv()

        replies = random.randint(0, 10)
        logging.info('send %s replies to %s [%s]', replies, identity, content)
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
    threading.Thread(target=tick_task, daemon=True).start()

    threading.Thread(target=client_task, daemon=True).start()
    threading.Thread(target=client_task, daemon=True).start()
    threading.Thread(target=client_task, daemon=True).start()

    threading.Thread(target=server_task, daemon=True).start()

    time.sleep(100)
    logging.info('done')
