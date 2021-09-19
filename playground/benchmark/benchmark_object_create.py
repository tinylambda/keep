import logging
import sys
import time

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


class User:
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age


if __name__ == '__main__':
    n = 1000000
    start = time.perf_counter()
    objects = [User('felix', 20) for i in range(n)]
    end = time.perf_counter()
    logging.info('cost %s', end - start)
