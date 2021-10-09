import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    # Syntactic sugar for default=attr.Factory(factory).
    f = attr.ib(factory=list)


if __name__ == '__main__':
    c = C()
    logging.info('%s', c.f)
