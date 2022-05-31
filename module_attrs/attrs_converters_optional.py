import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    x = attr.ib(converter=attr.converters.optional(int))


if __name__ == "__main__":
    c = C(None)
    logging.info("%s", c)
