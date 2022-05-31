import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s(slots=True)
class Coordinates:
    x = attr.ib()
    y = attr.ib()


if __name__ == "__main__":
    c = Coordinates(1, 2)
    logging.info("%s", dir(c))
