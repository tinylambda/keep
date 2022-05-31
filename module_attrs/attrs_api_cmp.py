import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s(cmp=True)
class C:
    x = attr.ib()
    y = attr.ib()


@attr.s(cmp=False)
class C2:
    x = attr.ib()
    y = attr.ib()


if __name__ == "__main__":
    c_1 = C(100, 100)
    c_2 = C(100, 100)
    c_3 = C(100, 200)

    logging.info("%s", c_1 == c_2)
    logging.info("%s", c_1 == c_3)

    c_1 = C2(100, 100)
    c_2 = C2(100, 100)
    c_3 = C2(100, 200)

    logging.info("%s", c_1 == c_2)
    logging.info("%s", c_1 == c_3)
