import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s(repr=False)
class A:
    x = attr.ib(type=int)


@attr.s(repr=True)
class B:
    x = attr.ib(type=int)


if __name__ == "__main__":
    a = A(100)
    b = B(100)
    logging.info("%s", a)
    logging.info("%s", b)
