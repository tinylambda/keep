import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    x = attr.ib(init=False)
    y = attr.ib(init=True)


if __name__ == '__main__':
    c = C(200)
    logging.info('%s', c)
    c.x = 100
    logging.info('%s', c)
