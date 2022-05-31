import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


def on_setter(instance, attribute, new_value):
    if new_value < 0:
        raise ValueError("value should be > 0")


@attr.s
class C:
    x = attr.ib(on_setattr=on_setter)


if __name__ == "__main__":
    c = C(-10)
    logging.info("%s", c)

    try:
        c.x = -1
    except ValueError:
        logging.error("error happened")
