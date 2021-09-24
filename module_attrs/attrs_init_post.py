import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    x = attr.ib()
    y = attr.ib(init=False)

    def __attrs_post_init__(self):
        self.y = self.x + 1


if __name__ == '__main__':
    c = C(1)
    logging.info('%s', c)
