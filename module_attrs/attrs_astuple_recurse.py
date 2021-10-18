import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class Point:
    x = attr.ib()
    y = attr.ib()


@attr.s
class Coordinator:
    p1 = attr.ib()
    p2 = attr.ib()


if __name__ == '__main__':
    coordinator = Coordinator(Point(1, 2), Point(0, 0))
    logging.info('%s', attr.astuple(coordinator, recurse=False))
    logging.info('%s', attr.astuple(coordinator, recurse=True))
