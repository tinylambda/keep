import collections

from memory_profiler import profile

Foobar = collections.namedtuple('Foobar', ['x'])


@profile
def main():
    f = [Foobar(42) for i in range(100000)]


if __name__ == '__main__':
    main()

# python -m memory_profiler books/sp/ch10/ch10_memory_namedtuple.py
