import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


def check(instance, attrib, new_value):
    if new_value < 0:
        raise RuntimeError("require %s >= 0" % attrib.name)
    return new_value


@attr.s
class C:
    x = attr.ib(validator=check)
    y = attr.ib()


if __name__ == "__main__":
    logging.info("%s", attr.fields(C).x)
    c = C(-1, 2)  # error
    logging.info("%s", c)
