import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class User:
    login = attr.ib()
    password = attr.ib()
    id = attr.ib()


@attr.s
class C:
    x = attr.ib()
    y = attr.ib()
    z = attr.ib()


if __name__ == '__main__':
    logging.info('%s', attr.asdict(User('hello', 'world', 42),
                                   filter=attr.filters.exclude(attr.fields(User).password, int)))
    logging.info('%s', attr.asdict(C('foo', '2', 3),
                                   filter=attr.filters.include(int, attr.fields(C).x)))
