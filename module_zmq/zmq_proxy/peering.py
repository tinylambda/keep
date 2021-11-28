import logging
import random
import sys
import threading
import time

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


def tick_task(interval=1):
    ctx = zmq.Context()
    publisher = ctx.socket(zmq.PUB)
    publisher.bind('ipc://tick_go')

    while True:
        publisher.send(b'K', zmq.SNDMORE)
        publisher.send(b'V')
        time.sleep(interval)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        logging.error('syntax: peering me {you}...')
        sys.exit()

    # first of all start the tick server
    threading.Thread(target=tick_task, args=(1, ), daemon=True).start()

    self = sys.argv[1]
    logging.info('I: preparing broker at %s', self)

    context = zmq.Context()
    # bind backend state to an endpoint
    state_be = context.socket(zmq.PUB)
    state_be.bind(f'ipc://{self}-state.ipc')

    # bind state_fe to all
    state_fe = context.socket(zmq.SUB)
    state_fe.setsockopt(zmq.SUBSCRIBE, b'')

    tick_source = context.socket(zmq.SUB)
    tick_source.setsockopt(zmq.SUBSCRIBE, b'')
    tick_source.connect('ipc://tick_go')

    for peer in sys.argv[2:]:
        logging.info(f'I: connecting to sate backend at {peer}')
        state_fe.connect(f'ipc://{peer}-state.ipc')

    poller = zmq.Poller()
    poller.register(state_fe, zmq.POLLIN)
    poller.register(tick_source, zmq.POLLIN)

    while True:
        try:
            sock_list = poller.poll(timeout=1 * 1000)  # milliseconds
        except Exception as e:
            logging.error('something wrong happened', e)
            break

        for sock, mask in sock_list:
            if sock == state_fe:
                peer_name = state_fe.recv()
                available = state_fe.recv()
                logging.info('%s - %s workers free', peer_name.decode(), available.decode())
            elif sock == tick_source:
                tick_source.recv()
                tick_source.recv()
                state_be.send(self.encode(), zmq.SNDMORE)
                state_be.send(f'{random.randint(1, 20)}'.encode())


# python peering.py x y z
# python peering.py y z x
