import logging
import sys
from array import array

import attr
import numpy

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s(order=False)
class C:
    an_array = attr.ib(eq=attr.cmp_using(eq=numpy.array_equal))


if __name__ == "__main__":
    c1 = C(array("i", [1, 2, 3]))
    c2 = C(array("i", [1, 2, 3]))

    logging.info("%s", c1 == c2)
