import time
import random

from queue import Queue
from threading import Thread


_sentinel = object()


def producer(out_q):
    for _ in range(10):
        data = random.randint(0, 3)
        time.sleep(data)
        out_q.put(data)
    out_q.put(_sentinel)


def consumer(in_q):
    while True:
        data = in_q.get()
        if data is _sentinel:
            in_q.put(_sentinel)
            print('consumer exit.')
            break
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

