import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s(kw_only=True)
class C:
    x = attr.ib()
    y = attr.ib()


if __name__ == '__main__':
    try:
        c = C(100, 200)
    except TypeError as e:
        logging.warning('error', exc_info=e)

    c = C(x=100, y=200)
    logging.info('%s', c)
