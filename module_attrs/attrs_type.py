import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    x = attr.ib(type=int)
    y: int = attr.ib()


if __name__ == '__main__':
    logging.info('%s', attr.fields(C).x.type)
    logging.info('%s', attr.fields(C).y.type)
