import logging
import sys

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    context = zmq.Context()

    frontend = context.socket(zmq.ROUTER)
    backend = context.socket(zmq.DEALER)

    frontend.bind('tcp://*:5559')
    backend.bind('tcp://*:5560')

    poller = zmq.Poller()
    poller.register(frontend, zmq.POLLIN)
    poller.register(backend, zmq.POLLIN)

    logging.info('starting broker')
    while True:
        socks = poller.poll()
        for sock, mask in socks:
            if sock == frontend:
                logging.info('forwarding request')

                while True:
                    message = sock.recv()
                    more = sock.getsockopt(zmq.RCVMORE)
                    backend.send(message, zmq.SNDMORE if more else 0)
                    if more == 0:
                        break
            elif sock == backend:
                logging.info('forwarding reply')
                while True:
                    message = sock.recv()
                    more = sock.getsockopt(zmq.RCVMORE)
                    frontend.send(message, zmq.SNDMORE if more else 0)
                    if more == 0:
                        break
