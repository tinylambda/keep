import functools
import math


@functools.lru_cache(maxsize=2)
def memoized_sin(x):
    return math.sin(x)


if __name__ == '__main__':
    print(memoized_sin(2))
    print(memoized_sin.cache_info())

    print(memoized_sin(2))
    print(memoized_sin.cache_info())

    print(memoized_sin(3))
    print(memoized_sin.cache_info())

    print(memoized_sin(4))
    print(memoized_sin.cache_info())

    print(memoized_sin(3))
    print(memoized_sin.cache_info())

    memoized_sin.cache_clear()
    print(memoized_sin.cache_info())
