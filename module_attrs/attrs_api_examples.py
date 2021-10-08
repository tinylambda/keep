import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    _private = attr.ib()


class D:
    def __init__(self, x):
        self.x = x


@attr.s(auto_exc=True)
class Error(Exception):
    x = attr.ib()
    y = attr.ib(default=42, init=False)


if __name__ == '__main__':
    c = C(private=87)
    logging.info('c: %s', c)
    logging.info('c._private: %s', getattr(c, '_private'))

    d = D(87)
    logging.info('d: %s', d)
    logging.info('d.x: %s', d.x)
    D = attr.s(these={'x': attr.ib()}, init=False)(D)
    d = D(87)
    logging.info('d: %s', d)
    logging.info('d.x: %s', d.x)

    e = Error('foo')
    logging.info('e: %s', e)
    raise Error('foo')
