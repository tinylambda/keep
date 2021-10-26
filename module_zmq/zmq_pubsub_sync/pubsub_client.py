import logging
import sys
import time

import zmq

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


def sync(connect_to: str):
    # use connect socket + 1
    parts = connect_to.split(':')
    pre = ':'.join(parts[:-1])
    port = int(parts[-1]) + 1
    sync_with = f'{pre}:{port}'
    ctx = zmq.Context.instance()
    s = ctx.socket(zmq.REQ)
    s.connect(sync_with)
    s.send(b'ready')
    s.recv()


if __name__ == '__main__':
    array_count = 10
    connect_to = 'tcp://localhost:5555'

    ctx = zmq.Context()
    s = ctx.socket(zmq.SUB)
    s.connect(connect_to)
    s.setsockopt(zmq.SUBSCRIBE, b'')

    sync(connect_to)

    start = time.process_time()

    for i in range(array_count):
        a = s.recv_pyobj()
    logging.info('done.')

    end = time.process_time()

    elapsed = end - start

    throughput = float(array_count) / elapsed
    message_size = a.nbytes
    megabits = float(throughput * message_size * 8) / 1000000

    logging.info('message size: %s B', message_size)
    logging.info('array_count: %s', array_count)
    logging.info('mean throughput: %s [msg/s]', throughput)
    logging.info('mean throughput: %s [Mb/s]', megabits)
