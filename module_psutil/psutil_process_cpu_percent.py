import logging
import sys
import threading

import psutil

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == "__main__":
    p = psutil.Process()

    logging.info("We start a sub thread first")

    def worker():
        i = 0
        while True:
            i += 1

    new_thread = threading.Thread(
        target=worker,
    )
    new_thread.daemon = True
    new_thread.start()

    logging.info("first call with no args = %s", p.cpu_percent())

    use_interval = 2
    logging.info(
        "call with a interval %s = %s", use_interval, p.cpu_percent(use_interval)
    )

    logging.info(
        "call with interval=None again <non-blocking (percentage since last call)> = %s",
        p.cpu_percent(interval=None),
    )
