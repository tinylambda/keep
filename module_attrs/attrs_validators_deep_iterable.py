import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    x = attr.ib(validator=attr.validators.deep_iterable(
        member_validator=attr.validators.instance_of(int),
        iterable_validator=attr.validators.instance_of(list)))


if __name__ == '__main__':
    c = C([1, 2, 3])
    logging.info('1. %s', c)

    try:
        c = C([1, 2, '3'])
        logging.info('2. %s', c)
    except TypeError as e:
        logging.error('value error', exc_info=e)

    try:
        c = C((1, 2, 3))
        logging.info('3. %s', c)
    except TypeError as e:
        logging.error('value error', exc_info=e)
