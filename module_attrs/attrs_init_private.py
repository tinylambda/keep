import inspect
import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    _x = attr.ib()


if __name__ == "__main__":
    signature = inspect.signature(C.__init__)
    logging.info("%s", signature)
