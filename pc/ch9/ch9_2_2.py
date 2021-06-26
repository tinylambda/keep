import time
from functools import wraps


def timethis(func):
    """decorator that reports the execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper


if __name__ == '__main__':
    @timethis
    def countdown(n: int):
        """counts down"""
        print('calling countdown')
        while n > 0:
            n -= 1

    countdown(10000)
    print(countdown.__name__)
    print(countdown.__doc__)
    print(countdown.__annotations__)

    print('-' * 64)

    countdown.__wrapped__(10000)

    from inspect import signature
    print(signature(countdown))

