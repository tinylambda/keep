import time
import random

from queue import Queue
from threading import Thread


def producer(out_q):
    while True:
        data = random.randint(0, 3)
        time.sleep(data)
        out_q.put(data)


def consumer(in_q):
    while True:
        data = in_q.get()
        print('processing', data)


if __name__ == '__main__':
    q = Queue()
    t1 = Thread(target=consumer, args=(q, ))
    t2 = Thread(target=producer, args=(q, ))
    t1.start()
    t2.start()

    print('join t1')
    t1.join()
    print('join t2')
    t2.join()

    print('done')

