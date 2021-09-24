import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


def x_smaller_than_y(instance, attribute, value):
    if value >= instance.y:
        raise ValueError('"x" has to be smaller than "y"')


@attr.s
class C:
    x = attr.ib(validator=[attr.validators.instance_of(int), x_smaller_than_y])
    y = attr.ib()


if __name__ == '__main__':
    c = C(x=3, y=4)
    logging.info('%s', c)

    try:
        c = C(x=4, y=3)
        logging.info('%s', c)
    except ValueError as e:
        logging.warning('error', exc_info=e)

    logging.info('%s', c)
    c.x = 5
    logging.info('%s', c)

    try:
        attr.validate(c)
    except ValueError as e:
        logging.warning('error: %s', e.args)
