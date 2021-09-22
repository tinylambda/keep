import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


C = attr.make_class('C', {
    'x': attr.ib(default=42),
    'y': attr.ib(default=attr.Factory(list)),
}, repr=False)

if __name__ == '__main__':
    i = C()
    logging.info('%s', i)
    logging.info('%s', i.x)
    logging.info('%s', i.y)
