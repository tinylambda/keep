import threading
import time

from ch12_5_2 import acquire


x_lock = threading.Lock()
y_lock = threading.Lock()


def thread_1():
    while True:
        with acquire(x_lock):
            with acquire(y_lock):
                print("Thread-1")


def thread_2():
    while True:
        with acquire(y_lock):
            with acquire(x_lock):
                print("Thread-2")


if __name__ == "__main__":
    t1 = threading.Thread(target=thread_1)
    t1.daemon = True
    t1.start()

    t2 = threading.Thread(target=thread_2)
    t2.daemon = True
    t2.start()

    time.sleep(1)
