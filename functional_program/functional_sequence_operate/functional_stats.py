import math
from collections import Sequence
# from typing import Sequence


def mean(items: Sequence):
    return sum(items) / len(items)


def z(x, mu_x: float, rou_x: float) -> float:
    return (x - mu_x) / rou_x


if __name__ == '__main__':
    data = range(10)

    def g():
        for i in range(10):
            yield i

    s0 = sum(x ** 0 for x in g())
    s1 = sum(x ** 1 for x in g())
    s2 = sum(x ** 2 for x in g())

    mean_ = s1 / s0
    stdev_ = math.sqrt(s2 / s0 - (s1 / s0) ** 2)

    print(mean_, stdev_)

    d = [2, 4, 4, 4, 5, 5, 7, 9]
    d_s0 = sum(x ** 0 for x in d)
    d_s1 = sum(x ** 1 for x in d)
    d_s2 = sum(x ** 2 for x in d)

    mean_d = d_s1 / d_s0
    stdev_d = math.sqrt(d_s2 / d_s0 - (d_s1 / d_s0) ** 2)

    print(
        list(z(x, mean_d, stdev_d) for x in d)
    )

