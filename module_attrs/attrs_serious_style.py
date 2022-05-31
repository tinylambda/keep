import logging
import sys

import attr
from attr import attrib

from module_attrs.attrs_with_attrs import Coordinates

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class SeriousCoordinates:
    x = attrib()
    y = attrib()


if __name__ == "__main__":
    c1 = SeriousCoordinates(1, 2)
    c2 = SeriousCoordinates(x=2, y=1)
    logging.info("%s", c1)
    logging.info("%s", c2)
    logging.info("%s", c1 == c2)

    logging.info("%s", attr.fields(SeriousCoordinates) == attr.fields(Coordinates))
