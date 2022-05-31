import logging
import sys
import time

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

if __name__ == "__main__":
    n = 10000000
    i = 0
    s = 0
    start = time.perf_counter()
    while i < n:
        s += 1
        i += 1
    end = time.perf_counter()
    logging.info("cost %s", end - start)
