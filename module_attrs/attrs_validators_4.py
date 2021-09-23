import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


def check(instance, attrib, new_value):
    if new_value < 0:
        raise RuntimeError('require %s >= 0' % attrib.name)
    return new_value


@attr.s(on_setattr=check)
class C:
    x = attr.ib()
    y = attr.ib()


if __name__ == '__main__':
    c = C(-1, 2)  # this is OK
    logging.info('%s', c)
    c.x = 20
    logging.info('%s', c)
    c.x = -1  # but this will trigger RuntimeError, seems weird.
    logging.info('%s', c)