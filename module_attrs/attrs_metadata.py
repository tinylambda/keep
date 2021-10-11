import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    x = attr.ib(metadata={'my_metadata': 1})

    def hello(self):
        logging.info('%s my value is %s', 'world', self.x)
        logging.info('%s', attr.fields(self.__class__).x.metadata)


if __name__ == '__main__':
    logging.info('%s', attr.fields(C).x.metadata)
    c = C(100)
    c.hello()