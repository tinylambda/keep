import time
from functools import wraps


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'{func.__module__}.{func.__name__} : {end - start}')
        return r
    return wrapper


@timethis
def countdown(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    countdown(10000000)
