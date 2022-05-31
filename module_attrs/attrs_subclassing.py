import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class A:
    a = attr.ib()

    def get_a(self):
        return self.a


@attr.s
class B:
    b = attr.ib()


@attr.s
class C(A, B):
    c = attr.ib()


if __name__ == "__main__":
    i = C(1, 2, 3)
    logging.info("%s", i)
    logging.info("%s", i.get_a())
