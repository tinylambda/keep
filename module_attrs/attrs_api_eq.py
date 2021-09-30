import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s(eq=False)
class A:
    x = attr.ib(type=int)
    y = attr.ib(type=int)


@attr.s(eq=True)
class B:
    x = attr.ib(type=int)
    y = attr.ib(type=int)


if __name__ == '__main__':
    a = A(100, 200)
    b = B(100, 300)

    logging.info('%s', a)
    logging.info('%s', b)

    a1 = A(100, 200)
    a2 = A(100, 200)
    logging.info('%s', a1 == a2)  # should be False

    # the following not supported
    # a3 = A(100, 200)
    # a4 = A(100, 300)
    # logging.info('%s', a3 > a4)
    # logging.info('%s', a3 < a4)

    b1 = B(100, 200)
    b2 = B(100, 200)
    logging.info('%s', b1 == b2)  # should be True

    logging.info('%s', b1 > b2)
    logging.info('%s', b1 < b2)

    b3 = B(100, 200)
    b4 = B(100, 300)
    logging.info('%s', b3 > b4)
    logging.info('%s', b3 < b4)
