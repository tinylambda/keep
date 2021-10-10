import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    x = attr.ib(cmp=True)
    y = attr.ib(cmp=lambda x: abs(x))


if __name__ == '__main__':
    c1 = C(100, -1)
    c2 = C(100, 1)

    logging.info('%s', c1 == c2)  # this should be True
    logging.info('%s', c1 > c2)
    logging.info('%s', c1 < c2)
