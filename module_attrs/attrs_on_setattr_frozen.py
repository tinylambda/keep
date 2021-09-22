import logging
import sys

import attr
from attr import setters

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


# the following will trigger ValueError, frozen classes cannot use on_setattr
@attr.s(frozen=True, on_setattr=setters.validate)
class C:
    x = attr.ib()


if __name__ == '__main__':
    pass
