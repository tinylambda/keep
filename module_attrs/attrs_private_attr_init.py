import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    _x = attr.ib(init=False, default=87)


if __name__ == '__main__':
    c = C()
    logging.info('%s', c)
    logging.info('%s', c._x)  # can access

    c = C(89)  # should raise an error

