import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


def check(*args, **kwargs):
    logging.info('args: %s ,kwargs: %s', args, kwargs)


@attr.s(on_setattr=check)
class C:
    x = attr.ib()
    y = attr.ib()


if __name__ == '__main__':
    c = C(1, 2)
    logging.info('%s', c)
    c.x = 100
