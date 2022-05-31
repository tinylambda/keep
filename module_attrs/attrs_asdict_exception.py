import logging
import sys

import attr
from attr.exceptions import NotAnAttrsClassError

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    x = attr.ib()
    y = attr.ib()


class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":
    c = C(1, 2)
    a = A(3, 4)
    logging.info("%s", attr.asdict(c))
    try:
        logging.info("%s", attr.asdict(a))
    except NotAnAttrsClassError as e:
        logging.error("not an attrs class error", exc_info=e)
