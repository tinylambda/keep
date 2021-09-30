import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s(order=False)
class A:
    x = attr.ib()


@attr.s(order=True)
class B:
    x = attr.ib()


if __name__ == '__main__':
    a1 = A(100)
    a2 = A(200)

    # the following not supported
    # logging.info('%s', a1 > a2)
    # logging.info('%s', a1 < a2)

    b1 = B(100)
    b2 = B(200)
    logging.info('%s', b1 > b2)
    logging.info('%s', b1 < b2)
