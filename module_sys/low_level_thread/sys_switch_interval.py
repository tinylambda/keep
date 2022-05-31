import sys
import threading
from queue import Queue


def show_thread(q):
    for i in range(5):
        for j in range(1000000):
            pass
        q.put(threading.current_thread().name)


def run_threads():
    interval = sys.getswitchinterval()
    print("interval = {:0.3f}".format(interval))

    q = Queue()
    threads = [
        threading.Thread(target=show_thread, name="T{}".format(i), args=(q,))
        for i in range(3)
    ]

    for t in threads:
        t.setDaemon(True)
        t.start()

    for t in threads:
        t.join()

    while not q.empty():
        print(q.get(), end=" ")
    print()


if __name__ == "__main__":
    for interval in [0.001, 0.1]:
        sys.setswitchinterval(interval)
        run_threads()
        print()

# Many factors other than the switch interval may control the context switching behavior of Python’s threads.
# For example, when a thread performs I/O it releases the GIL and may therefore allow another thread
# to take over execution.
