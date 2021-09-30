import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s(str=False)
class A:
    x = attr.ib(type=int)


@attr.s(str=True)
class B:
    x = attr.ib(type=int)


if __name__ == '__main__':
    a = A(100)
    b = B(100)

    logging.info('%s', a)
    logging.info('%s', b)

    logging.info('%s', str(a))
    logging.info('%s', str(b))

    # raise RuntimeError('error', a)
    # raise RuntimeError('error', b)
