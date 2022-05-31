import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    _x = attr.ib()


if __name__ == "__main__":
    c = C(x=1)
    logging.info("%s", c)
    logging.info("%s", c._x)  # can access
