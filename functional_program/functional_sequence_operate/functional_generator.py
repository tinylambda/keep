import math

from typing import Callable, Iterable, Any, Generator, Iterator


def first(predicate: Callable, collection: Iterable) -> Any:
    for x in collection:
        if predicate(x):
            return x


def isprime(x: int) -> bool:
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    factor = first(
        lambda n: x % n == 0,
        range(3, int(math.sqrt(x) + 0.5) + 1, 2)
    )

    return factor is None


def map_not_none(func: Callable, source: Iterable) -> Iterator:
    for x in source:
        try:
            yield func(x)
        except Exception as e:
            pass


if __name__ == '__main__':
    x1 = [1, 2, 3, 4]
    x2 = range(100)

    def x3():
        for i in range(100):
            yield i

    print(type(x1), type(x2))
    print(isinstance(x3(), Generator))

    greater_than_3: Callable = lambda x: x > 3

    print(first(greater_than_3, x1))
    print(first(greater_than_3, x2))
    print(first(greater_than_3, x3()))

    print(isprime(7))

    x4 = [1, 100, -1, 10000]
    r = map_not_none(math.sqrt, x4)
    print(list(r))

    x5 = ['10', 'abc', '20', '34', '45y']
    r2 = map_not_none(int, x5)
    print(list(r2))

