import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class A:
    a = attr.ib(kw_only=True)


if __name__ == '__main__':
    a = A(a=1)
    logging.info('%s', a)

    try:
        a = A()
    except TypeError as e:
        logging.error('error', exc_info=e)

    try:
        a = A(1)   # raise a TypeError
    except TypeError as e:
        logging.error('error', exc_info=e)
