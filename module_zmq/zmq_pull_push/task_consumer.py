import logging
import sys
import time

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    context = zmq.Context()

    # socket to receive messages on
    receiver = context.socket(zmq.PULL)
    receiver.connect('tcp://localhost:5557')

    # socket to send messages to
    sender = context.socket(zmq.PUSH)
    sender.connect('tcp://localhost:5558')

    # controller
    controller = context.socket(zmq.SUB)
    controller.connect('tcp://localhost:5559')
    controller.setsockopt(zmq.SUBSCRIBE, b'')

    poller = zmq.Poller()
    poller.register(receiver, zmq.POLLIN)
    poller.register(controller, zmq.POLLIN)

    # while True:
    #     message = receiver.recv()
    #     logging.info('received message %s', message)
    #     workload = int(message.decode())
    #     time.sleep(workload / 1000.)
    #
    #     sender.send(b'')

    exit_sys = False

    while True:
        socks = poller.poll()
        for sock, mask in socks:
            if sock == receiver:
                message = sock.recv()
                logging.info('received message %s', message)
                workload = int(message.decode())
                time.sleep(workload / 1000.)
                sender.send(b'')
            elif sock == controller:
                exit_sys = True

        if exit_sys:
            logging.info('exiting...')
            break
