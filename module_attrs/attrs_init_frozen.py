import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s(frozen=True)
class FrozenBroken:
    x = attr.ib()
    y = attr.ib(init=False)

    # def __attrs_post_init__(self):
    #     self.y = self.x + 1

    def __attrs_post_init__(self):
        object.__setattr__(self, 'y', self.x + 1)


if __name__ == '__main__':
    fb = FrozenBroken(1)
    logging.info('%s', fb)
