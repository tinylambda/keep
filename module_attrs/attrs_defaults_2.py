import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    x = attr.ib(default=1)
    y = attr.ib()

    @y.default
    def _any_name_except_a_name_of_an_attribute(self):
        return self.x + 1


@attr.s
class C1:
    x = attr.ib(factory=list)


if __name__ == "__main__":
    c1 = C1()
    logging.info("%s", c1)
