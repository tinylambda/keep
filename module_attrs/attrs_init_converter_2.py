import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


def validate_x(instance, attribute, value):
    if value < 0:
        raise ValueError("x must be at least 0")


def str2int(x: str):
    return int(x)


@attr.s
class C:
    x = attr.ib(converter=str2int, validator=validate_x)


if __name__ == "__main__":
    c = C("1")
    logging.info("%s", c.x)

    try:
        c = C("-1")
    except ValueError as e:
        logging.error("error", exc_info=e)

    logging.info("%s", C.__init__.__annotations__)
