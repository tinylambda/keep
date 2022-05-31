import threading
import logging
import time


class MyThread(threading.Thread):
    def run(self) -> None:
        time.sleep(0.1 * 10)
        logging.debug("running")


logging.basicConfig(level=logging.DEBUG, format="(%(threadName)-10s) %(message)s")

for i in range(5):
    t = MyThread(daemon=False)
    t.start()
