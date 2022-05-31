import logging
import sys
from collections import namedtuple

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


class PointBad:
    def __init__(self, database_row):
        self.x = database_row.x
        self.y = database_row.y


@attr.s
class PointGood:
    x = attr.ib()
    y = attr.ib()

    @classmethod
    def from_row(cls, row):
        return cls(row.x, row.y)


if __name__ == "__main__":
    Row = namedtuple("Row", "x,y")
    pb = PointBad(Row(x=1, y=2))
    logging.info("x = %s, y = %s", pb.x, pb.y)

    pg = PointGood.from_row(Row(x=1, y=2))
    logging.info("%s", pg)
