import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class Foo:
    a = attr.ib()
    b = attr.ib()


if __name__ == '__main__':
    foo = Foo(2, 3)
    logging.info('%s', attr.astuple(foo))
