import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


def x_smaller_than_y(instance, attribute, value):
    logging.info('attribute is %s', attribute)
    if value >= instance.y:
        raise ValueError('x has to be smaller than y')


@attr.s
class C:
    x = attr.ib(validator=[attr.validators.instance_of(int), x_smaller_than_y])
    y = attr.ib()


if __name__ == '__main__':
    c = C(x=3, y=4)
    logging.info('%s', c)
    c = C(x=4, y=3)
    logging.info('%s', c)
