import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class T:
    a = attr.ib()
    b = attr.ib()


@attr.s
class C:
    x = attr.ib()
    y = attr.ib(type=T)


if __name__ == '__main__':
    logging.info('%s', attr.fields(C))
    logging.info('%s', attr.fields(C)[1])
    logging.info('%s', attr.fields(C).y)

    attr_y = attr.fields(C).y
    logging.info('%s', attr_y.type)
