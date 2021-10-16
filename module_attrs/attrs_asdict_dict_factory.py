import collections
import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    x = attr.ib()
    y = attr.ib()


if __name__ == '__main__':
    c = C(1, 2)
    r1 = attr.asdict(c)
    r2 = attr.asdict(c, dict_factory=collections.OrderedDict)
    logging.info('%s, %s', r1, type(r1))
    logging.info('%s, %s', r2, type(r2))
    