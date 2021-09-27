import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class S:
    x = attr.ib(eq=str.lower)


@attr.s
class C:
    x = attr.ib(order=int)


if __name__ == '__main__':
    logging.info('%s', S('FOO') == S('foo'))  # should be True
    logging.info('%s', C('10') > C('2'))  # should be True
