import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class A:
    a = attr.ib(default=0)


@attr.s
class B(A):
    b = attr.ib(kw_only=True)


if __name__ == '__main__':
    # keyword-only attributes allow subclasses to add attributes without default values, even if the abse class
    # defines attributes with default values
    b = B(b=1)
    logging.info('%s', b)

    try:
        b = B()
    except TypeError as e:
        logging.error('error', exc_info=e)
