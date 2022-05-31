import random
import time

from queue import Queue
from threading import Thread, Event


def producer(out_q):
    for _ in range(10):
        data = random.randint(0, 3)
        time.sleep(data)
        out_q.put(data)


def consumer(in_q):
    while True:
        data = in_q.get()
        print("processing", data)
        in_q.task_done()


if __name__ == "__main__":
    q = Queue()
    finished = Event()

    t1 = Thread(target=consumer, args=(q,))
    t2 = Thread(target=producer, args=(q,))
    t1.start()
    t2.start()

    print("join q")
    q.join()
    print("done")
