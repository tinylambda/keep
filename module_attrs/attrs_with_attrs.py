import logging
import sys

import attr


logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class Coordinates:
    x = attr.ib()
    y = attr.ib()


if __name__ == "__main__":
    c1 = Coordinates(1, 2)
    c2 = Coordinates(x=2, y=1)
    logging.info("%s", c1)
    logging.info("%s", c2)
    logging.info("%s", c1 == c2)
