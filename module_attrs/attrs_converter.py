import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    x = attr.ib(converter=int)


if __name__ == '__main__':
    o = C('1')
    logging.info('%s: %s', o.x, type(o.x))

