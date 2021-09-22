import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    x = attr.ib()
    y = attr.ib()
    z = attr.ib(init=False)

    def __attrs_post_init__(self):
        self.z = self.x + self.y


if __name__ == '__main__':
    obj = C(x=1, y=2)
    logging.info('%s', obj)
