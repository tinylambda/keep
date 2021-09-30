import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s(these={'x': attr.ib(init=False)})
class C:
    y = attr.ib()


if __name__ == '__main__':
    c = C()
    c.x = 200
    c.y = 300
    # If these is not None,
    # attrs will not search the class body for attributes and will not remove any attributes from it.
    logging.info('%s', attr.fields(C))
    logging.info('%s', c)
