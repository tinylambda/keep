import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    x = attr.ib()


if __name__ == "__main__":
    logging.info("%s", attr.fields(C).x)  # Read-only representation of an attribute.
