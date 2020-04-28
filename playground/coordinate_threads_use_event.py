import threading
import time
import logging


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s'
)


def worker(event):
    logging.debug('Waiting for redis ready...')
    event.wait()
    logging.debug('Redis ready!')
    time.sleep(1)  # Simulate workload


redis_ready = threading.Event()
t1 = threading.Thread(target=worker, args=(redis_ready,), name='redis_waiter_1')
t1.start()

t2 = threading.Thread(target=worker, args=(redis_ready,), name='redis_waiter_2')
t2.start()

logging.debug('Check Redis....')
time.sleep(3)  # Check redis...
logging.debug('Redis service is OK now! notify all workers!')
redis_ready.set()

