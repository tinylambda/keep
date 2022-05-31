import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    x = attr.ib()
    y = attr.ib()


if __name__ == "__main__":
    c = C(1, 2)
    logging.info("%s", attr.astuple(c, tuple_factory=list))
    logging.info("%s", attr.astuple(c, tuple_factory=list))
