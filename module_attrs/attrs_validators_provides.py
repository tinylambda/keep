import logging
import sys

import attr
from zope.interface import Interface, implementer

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


class Computer(Interface):
    def compute(self, num):
        """compute with arg num"""


class BadCompute:
    def compute(self, num):
        logging.info('bad implement')


@implementer(Computer)
class GoodCompute:
    def compute(self, num):
        for i in range(num):
            logging.info('computing %s', i)


@attr.s
class C:
    a = attr.ib(type=Computer, validator=attr.validators.provides(Computer))


if __name__ == '__main__':
    c = C(GoodCompute())
    logging.info('%s', c)
    c.a.compute(10)

    try:
        c = C(BadCompute())
    except TypeError as e:
        logging.error('type error')
