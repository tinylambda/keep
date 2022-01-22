import logging
import sys
import threading
import time

import psutil

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':

    logging.info('We start a sub thread first')

    def worker():
        i = 0
        while True:
            i += 1
            if i % 10000000 == 0:
                logging.info('switch...')
                time.sleep(0.01)

    new_thread = threading.Thread(target=worker,)
    new_thread.daemon = True
    new_thread.start()

    cpu_count = psutil.cpu_count()
    logging.info('cpu_count = %s', cpu_count)

    p = psutil.Process()
    logging.info('cpu_affinity = %s', p.cpu_affinity())
    time.sleep(10)

    p.cpu_affinity([0, 1])
    logging.info('process will now only run on CPU 0 and 1')
    logging.info('cpu_affinity = %s', p.cpu_affinity())
    time.sleep(10)

    p.cpu_affinity([])
    logging.info('process will now run all eligible CPUs')
    logging.info('cpu_affinity = %s', p.cpu_affinity())
    time.sleep(10)
