import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    x = attr.ib()

    @x.validator
    def check(self, attribute, value):
        if value > 42:
            raise ValueError('x must be smaller or equal to 42')


if __name__ == '__main__':
    c = C(42)
    logging.info('%s', c)
    c1 = C(43)  # this will trigger ValueError
    logging.info('%s', c)
