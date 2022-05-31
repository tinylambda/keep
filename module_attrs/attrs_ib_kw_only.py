import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    x = attr.ib(kw_only=True)
    y = attr.ib()


if __name__ == "__main__":
    c = C(100, x=20)
    logging.info("%s", c)
