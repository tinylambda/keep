import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    x = attr.ib(eq=True)
    y = attr.ib(eq=False)
    z = attr.ib(eq=lambda x: abs(x))


if __name__ == '__main__':
    c1 = C(100, 200, 1)
    c2 = C(100, 300, -1)
    logging.info('should be True: %s', c1 == c2)
