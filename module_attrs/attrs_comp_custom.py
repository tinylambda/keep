import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    x = attr.ib()
    y = attr.ib(eq=False)


if __name__ == "__main__":
    logging.info("%s", C(1, 2) == C(1, 3))  # should be True
