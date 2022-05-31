import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


class D:
    def __eq__(self, other):
        return True


C = attr.make_class("C", {}, bases=(D,), order=False)

if __name__ == "__main__":
    logging.info("%s", isinstance(C(), D))
