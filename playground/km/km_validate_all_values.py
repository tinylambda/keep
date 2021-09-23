import logging
import sys

import attr
from attr import make_class

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


def state_check(instance, attrib, new_value):
    attr_fullname = f'{instance.__class__.__name__}.{attrib.name}'
    logging.info(f'checking for {attr_fullname}...')
    if new_value < 0:
        raise RuntimeError('require %s >= 0' % attrib.name)
    return new_value


x = make_class('C', {
    'x': attr.ib(validator=state_check, default=-1),
    'y': attr.ib(validator=state_check, default=0),
}, kw_only=True)

if __name__ == '__main__':
    # we can register each class in a global dict
    logging.info('%s', x.__name__)
