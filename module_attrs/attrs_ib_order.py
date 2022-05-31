import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    x = attr.ib(order=True)
    y = attr.ib(order=True)
    # we can use cmp to set eq and order to the same value
    z = attr.ib(order=lambda x: abs(x), eq=lambda x: abs(x))


if __name__ == "__main__":
    c1 = C(100, 200, 1)
    c2 = C(100, 88, 1)
    c3 = C(100, 200, 1)
    c4 = C(100, 200, -1)
    l = [c1, c2]
    logging.info("%s", c1 > c2)
    logging.info("%s", c1 == c2)
    logging.info("%s", c1 < c2)

    logging.info("%s", c1 == c3)
    logging.info("%s", c3 == c4)
