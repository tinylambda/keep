import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    x = attr.ib(validator=attr.validators.is_callable())


if __name__ == '__main__':
    c = C(isinstance)
    logging.info('%s', c)

    try:
        c = C(87)
    except ValueError as e:
        logging.error('value error', exc_info=e)
