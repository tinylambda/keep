import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    x = attr.ib()

    def __attrs_pre_init__(self):
        super().__init__()


if __name__ == '__main__':
    c = C(42)
    logging.info('%s', c)
