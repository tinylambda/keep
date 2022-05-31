import random
import time

from queue import Queue
from threading import Thread, Event

_sentinel = object()


def producer(out_q):
    for _ in range(10):
        evt = Event()
        data = random.randint(0, 3)
        time.sleep(data)
        print("produced: ", data)
        out_q.put((data, evt))
        evt.wait()
        print("consumed: ", data)

    out_q.put((_sentinel, None))


def consumer(in_q):
    while True:
        data, evt = in_q.get()
        if data is _sentinel:
            in_q.put((_sentinel, None))
            print("bye.")
            break
        print("processing", data)
        evt.set()


if __name__ == "__main__":
    q = Queue()
    finished = Event()

    t1 = Thread(target=consumer, args=(q,))
    t2 = Thread(target=producer, args=(q,))
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("done")
