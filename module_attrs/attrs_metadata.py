import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    x = attr.ib(metadata={'my_metadata': 1})


if __name__ == '__main__':
    logging.info('%s', attr.fields(C).x.metadata)
