import logging
import sys

import attr
from attr.exceptions import NotAnAttrsClassError

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


"""
private attributes should be specified without the leading underscore, just like in __init__.

attributes with init=False can’t be set with evolve.

the usual __init__ validators will validate the new values.
"""


@attr.s(frozen=True)
class C:
    x = attr.ib()
    y = attr.ib()


class X:
    def __init__(self, x):
        self.x = x


if __name__ == "__main__":
    i1 = C(1, 2)
    logging.info("%s", i1)
    i2 = attr.evolve(i1, y=3)
    logging.info("%s", i2)
    logging.info("%s", i1 == i2)
    try:
        i3 = attr.evolve(i2, z=100)
    except TypeError as e:
        logging.error("type error", exc_info=e)

    x1 = X(1)
    try:
        x2 = attr.evolve(x1, x=2)
    except NotAnAttrsClassError as e:
        logging.error("NotAnAttrsClassError", exc_info=e)

    Y = attr.s(these={"x": attr.ib()})(X)
    y1 = Y(1)
    y2 = attr.evolve(y1, x=3)
    logging.info("%s -> %s", y1, y2)
