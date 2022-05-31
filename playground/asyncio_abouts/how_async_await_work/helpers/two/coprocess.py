import pickle
import subprocess
import sys

from concurrent.futures import ProcessPoolExecutor
from coroutine import coroutine
from cofollow import follow, printer


@coroutine
def sendto(f):
    try:
        while True:
            item = yield
            pickle.dump(item, f)
            f.flush()
    except StopIteration:
        f.close()


def recvfrom(f, target):
    try:
        while True:
            item = pickle.load(f)
            target.send(item)
    except EOFError:
        target.close()


if __name__ == "__main__":
    pass
