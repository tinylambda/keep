import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class X:
    @attr.s(repr_ns='OUTER_X')
    class C:
        m = attr.ib()
        n = attr.ib()

    a = attr.ib()
    b = attr.ib()


if __name__ == '__main__':
    x = X(100, 200)
    c = X.C('hello', 'world')

    logging.info('%s', x)
    logging.info('%s', c)
