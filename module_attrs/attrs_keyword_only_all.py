import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s(kw_only=True)
class A:
    a = attr.ib()
    b = attr.ib()


if __name__ == "__main__":
    try:
        a = A(1, 2)
    except TypeError as e:
        logging.info("error", exc_info=e)

    a = A(a=1, b=2)
    logging.info("%s", a)
