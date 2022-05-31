import enum
import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


class State(enum.Enum):
    ON = "on"
    OFF = "off"


@attr.s
class C:
    mixed = attr.ib(
        validator=attr.validators.and_(
            attr.validators.in_([1, 2, 3]), attr.validators.instance_of(int)
        )
    )
    # mixed = attr.ib(validator=[attr.validators.in_([1, 2, 3]), attr.validators.instance_of(int)])


if __name__ == "__main__":
    c = C(1)
    logging.info("%s", c)
    try:
        c = C(4)
    except ValueError as e:
        logging.error("value error", exc_info=e)

    try:
        c = C(1.0)
    except ValueError as e:
        logging.error("value error", exc_info=e)
