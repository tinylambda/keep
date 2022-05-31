import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    x = attr.ib(repr=True)
    y = attr.ib(repr=False)
    z = attr.ib(repr=lambda x: "Good %s" % x)


if __name__ == "__main__":
    c = C(100, 200, 300)
    logging.info("%s", repr(c))
    logging.info("%s", str(c))
    logging.info("%s", c)
