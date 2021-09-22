import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s(frozen=True)
class C:
    x = attr.ib()
    y = attr.ib()


if __name__ == '__main__':
    i1 = C(1, 2)
    logging.info('%s', i1)
    i2 = attr.evolve(i1, y=3)
    logging.info('%s', i2)
    logging.info('%s', i1 == i2)
