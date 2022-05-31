import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    complex = attr.ib(type=list[list[dict]])


if __name__ == "__main__":
    c = C(complex=[[{}, {}], [{}, {}]])
    logging.info("%s", c)
