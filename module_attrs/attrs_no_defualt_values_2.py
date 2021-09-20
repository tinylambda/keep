import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class A:
    a = attr.ib(default=10)


#  No mandatory attributes allowed after an attribute with a default value or factory.
@attr.s
class B(A):
    b = attr.ib()


if __name__ == '__main__':
    pass
