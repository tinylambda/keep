import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    x = attr.ib()

    @x.validator
    def check(self, attribute, value):
        if value > 42:
            raise ValueError("x must be smaller or equal to 42")


if __name__ == "__main__":
    attr.set_run_validators(False)
    c = C(42)
    logging.info("%s", c)
    c1 = C(43)  # this will trigger ValueError
    logging.info("%s", c)
    logging.info("%s", c1)
    logging.info("%s", attr.get_run_validators())

    attr.set_run_validators(True)
    c1 = C(43)
