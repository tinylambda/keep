import logging
import sys

import attr
from attr import setters
from attr.exceptions import FrozenAttributeError

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s(on_setattr=setters.frozen)
class C:
    x = attr.ib()


if __name__ == "__main__":
    c = C(100)
    logging.info("%s", c)
    try:
        c.x = 200  # trigger FrozenAttributeError
    except FrozenAttributeError as e:
        logging.error("it happened")
