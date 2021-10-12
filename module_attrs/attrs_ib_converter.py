import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    x = attr.ib(converter=lambda x: int(x))


if __name__ == '__main__':
    c = C('1002')
    logging.info('%s %s', type(c.x), c)
