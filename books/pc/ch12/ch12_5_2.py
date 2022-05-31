import threading
import time
from contextlib import contextmanager


# Thread-local state to stored information on locks already acquired
_local = threading.local()


@contextmanager
def acquire(*locks):
    # sort locks by object identifier
    locks = sorted(locks, key=lambda x: id(x))

    # make sure lock order of previously acquired locks is not violated
    acquired = getattr(_local, "acquired", [])
    if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):
        raise RuntimeError("lock order violation")

    # acquire all of the locks
    acquired.extend(locks)
    _local.acquired = acquired

    try:
        for lock in locks:
            lock.acquire()
        yield
    finally:
        # release locks in reverse order of acquisition
        for lock in reversed(locks):
            lock.release()
        del acquired[-len(locks) :]


if __name__ == "__main__":
    import threading

    x_lock = threading.Lock()
    y_lock = threading.Lock()

    def thread_1():
        while True:
            with acquire(x_lock, y_lock):
                print("Thraed-1")

    def thread_2():
        while True:
            with acquire(y_lock, x_lock):
                print("Thread-2")

    t1 = threading.Thread(target=thread_1)
    t1.daemon = True
    t1.start()

    t2 = threading.Thread(target=thread_2)
    t2.daemon = True
    t2.start()

    time.sleep(10)
