import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    x = attr.ib(type=int)
    # In Python 3.6 or greater, the preferred method to specify the type is using a variable annotation
    y: int = attr.ib()


if __name__ == "__main__":
    c = C(100, 200)
    logging.info("%s", c)
    logging.info("%s %s", type(c.x), type(c.y))
