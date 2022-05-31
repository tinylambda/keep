from functools import reduce
from operator import mul


def f(n):
    return reduce(mul, range(1, n + 1))


if __name__ == "__main__":
    print(f(40))
