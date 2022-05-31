import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    x = attr.ib(converter=attr.converters.default_if_none(factory=lambda: 200))
    y = attr.ib(converter=attr.converters.default_if_none(100))


if __name__ == "__main__":
    c = C(None, None)
    logging.info("%s", c)
