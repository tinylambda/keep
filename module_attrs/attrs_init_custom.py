import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s(auto_detect=True)  # or init=False
class C:
    x = attr.ib()

    def __init__(self, x: int = 42):
        self.__attrs_init__(x)


if __name__ == '__main__':
    c = C()
    logging.info('%s', c)
