import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    x = attr.ib(validator=[attr.validators.instance_of(int)])

    @x.validator
    def fits_byte(self, attribute, value):
        if not 0 <= value < 256:
            raise ValueError('value out of bounds')


if __name__ == '__main__':
    try:
        c = C('128')
    except TypeError as e:
        logging.error('error', exc_info=e)

    try:
        c = C(256)
    except ValueError as e:
        logging.error('error', exc_info=e)
