import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    @attr.s(repr_ns='C')
    class D:
        pass


if __name__ == '__main__':
    d = C.D()
    logging.info('%s', d)
