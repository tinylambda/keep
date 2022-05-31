import logging
import sys

import attr
from attr import setters

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s(on_setattr=setters.validate)
class C:
    x = attr.ib(validator=attr.validators.instance_of(str))


if __name__ == "__main__":
    c = C("199")
    logging.info("%s", c)

    try:
        c = C(199)
        logging.info("%s", c)
    except TypeError as e:
        logging.error("it happened")
