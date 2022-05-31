import time
from contextlib import contextmanager


@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print("{}: {}".format(label, end - start))


with timethis("counting"):
    n = 100000000
    while n > 0:
        n -= 1
