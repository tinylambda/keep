import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    # Syntactic sugar for default=attr.Factory(factory).
    f = attr.ib(factory=list)
    x = attr.ib(default=attr.Factory(list))
    y = attr.ib(default=attr.Factory(lambda self: set(self.x), takes_self=True))


if __name__ == '__main__':
    c = C(x=[1, 2, 3])
    logging.info('%s', c)
    logging.info('%s', c.f)


