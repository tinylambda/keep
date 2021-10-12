import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s(frozen=True)
class C:
    x = attr.ib(hash=True)
    y = attr.ib(hash=False)


if __name__ == '__main__':
    c1 = C(100, 200)
    c2 = C(100, 300)
    c3 = C(101, 200)

    logging.info('%s', hash(c1) == hash(c2))  # True
    logging.info('%s', hash(c1) == hash(c3))  # False
