import time
from contextlib import contextmanager


@contextmanager
def timeblock(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        print(f'{label} : {end - start}')


if __name__ == '__main__':
    with timeblock('counting'):
        n = 10000000
        while n > 0:
            n -= 1
