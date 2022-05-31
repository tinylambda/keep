import itertools
from typing import Iterable, Any


def limits(iterable: Iterable[Any]) -> Any:
    max_tee, min_tee = itertools.tee(iterable, 2)
    return max(max_tee), min(min_tee)


def numbers():
    for i in range(10):
        yield i


if __name__ == "__main__":
    ns = numbers()
    print(limits(ns))
