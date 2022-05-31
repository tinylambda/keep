import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    a = attr.ib()
    x = attr.ib(default=87)
    y = attr.ib(default=21, init=False)
    f = attr.ib(default=attr.Factory(list))


if __name__ == "__main__":
    c = C(a=10)
    logging.info("%s", c.x)
    logging.info("%s", c.y)
    logging.info("%s", c.a)
    logging.info("%s, (%s)", c.f, id(c.f))

    c = C(10, x=1987)
    logging.info("%s", c.x)
    logging.info("%s", c.y)
    logging.info("%s", c.a)
    logging.info("%s, (%s)", c.f, id(c.f))
