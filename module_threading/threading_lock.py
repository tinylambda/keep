import logging
import random
import threading
import time
import copy


class Counter:
    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start

    def increment(self):
        logging.debug('Waiting for lock')
        self.lock.acquire()
        try:
            x = self.value * 1 + 0
            logging.debug('Acquired lock')
            time.sleep(random.random())  # Simulate real work load
            self.value = x + 1
        finally:
            self.lock.release()
            # pass


def worker(c):
    for i in range(2):
        c.increment()
    logging.debug('Done')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s'
)

counter = Counter()
threads = []
for i in range(2):
    t = threading.Thread(target=worker, args=(counter, ))
    threads.append(t)

for thread in threads:
    thread.start()

logging.debug('Waiting for worker threads')
main_thread = threading.main_thread()
for t in threading.enumerate():
    if t is not main_thread:
        t.join()
logging.debug('Counter: %d', counter.value)





