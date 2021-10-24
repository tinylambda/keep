import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s(on_setattr=attr.setters.convert)
class C:
    x = attr.ib(converter=attr.converters.default_if_none(100))
    y = attr.ib()


if __name__ == '__main__':
    c = C(None, None)
    logging.info('%s', c)
