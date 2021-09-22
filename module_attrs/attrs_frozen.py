import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s(frozen=True)
class C:
    x = attr.ib()


if __name__ == '__main__':
    i = C(1)
    i.x = 2  # error
