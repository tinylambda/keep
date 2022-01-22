import logging
import sys
import threading
import time

import psutil

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    p = psutil.Process()

    logging.info('Before starting new thread: threads number = %s', p.num_threads())
    for thread in p.threads():
        logging.info('pid = %s, id = %s, user_time = %s, system_time = %s',
                     p.pid, thread.id, thread.user_time, thread.system_time)

    def worker():
        time.sleep(3)

    new_thread = threading.Thread(target=worker)
    new_thread.daemon = True
    new_thread.start()

    logging.info('After starting new thread: threads number = %s', p.num_threads())
    for thread in p.threads():
        logging.info('pid = %s, id = %s, user_time = %s, system_time = %s',
                     p.pid, thread.id, thread.user_time, thread.system_time)

    new_thread.join()

    logging.info('After new thread exiting: threads number = %s', p.num_threads())
    for thread in p.threads():
        logging.info('pid = %s, id = %s, user_time = %s, system_time = %s',
                     p.pid, thread.id, thread.user_time, thread.system_time)

    time.sleep(1)
    logging.info('After new thread exiting and sleep 1 seconds: threads number = %s', p.num_threads())

    logging.info('Done')
