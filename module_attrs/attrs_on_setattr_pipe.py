import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s(on_setattr=attr.setters.frozen)
class C:
    x = attr.ib()
    y = attr.ib(on_setattr=attr.setters.NO_OP)


if __name__ == '__main__':
    c = C(100, 200)
    logging.info('%s', c)

    c.y = 300
    logging.info('%s', c)

    try:
        c.x = 200
    except attr.exceptions.FrozenAttributeError:
        logging.error('it happened')
