import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    pass


if __name__ == '__main__':
    logging.info('%s', attr.has(C))
    logging.info('%s', attr.has(object))
