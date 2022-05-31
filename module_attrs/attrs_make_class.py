import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C1:
    x = attr.ib()
    y = attr.ib()


C2 = attr.make_class("C2", ["x", "y"])


if __name__ == "__main__":
    logging.info("%s", attr.fields(C1) == attr.fields(C2))
