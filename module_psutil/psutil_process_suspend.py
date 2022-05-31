import logging
import sys
import threading
import time

import psutil

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == "__main__":
    p = psutil.Process()

    logging.info("running pid = %s", p.pid)

    def worker():
        i = 0
        while True:
            i += 1
            if i % 100000000 == 0:
                logging.info("still working")

    new_thread = threading.Thread(target=worker)
    new_thread.daemon = True
    new_thread.start()

    # use top to observe the TIME+ column, threads in this process will also stop working
    time.sleep(10)

    logging.info("try to suspend pid = %s", p.pid)
    p.suspend()
    logging.info("can reach here ? try p.resume() in another process")
