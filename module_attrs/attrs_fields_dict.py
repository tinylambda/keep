import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    x = attr.ib()
    y = attr.ib()


if __name__ == '__main__':
    logging.info('%s', attr.fields_dict(C))
