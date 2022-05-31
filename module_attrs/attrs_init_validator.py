import inspect
import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    x = attr.ib()

    @x.validator
    def _check_x(self, attribute, value):
        logging.info("self is %s", self)
        logging.info("attribute is %s", attribute)
        if value > 42:
            raise ValueError("x must be smaller or equal to 42")


if __name__ == "__main__":
    c = C(42)
    logging.info("%s", c)

    try:
        c = C(43)  # error
    except ValueError as e:
        logging.warning("error happened", exc_info=e)

    signature = inspect.signature(C.__init__)
    logging.info("%s", signature)
