import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    x = attr.ib(converter=attr.converters.pipe(int, float))


if __name__ == "__main__":
    c = C(1.24)
    logging.info("%s", c)
