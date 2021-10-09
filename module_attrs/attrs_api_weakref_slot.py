import logging
import sys
import weakref

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s(weakref_slot=True, slots=True)
class C:
    x = attr.ib()
    y = attr.ib()


@attr.s(weakref_slot=False)
class A:
    x = attr.ib()
    y = attr.ib()


if __name__ == '__main__':
    d = weakref.WeakValueDictionary()
    c = C(100, 200)
    a = A(100, 200)
    logging.info('%s', c)
    d['x'] = c
    d['y'] = a
    logging.info('%s', d.get('x'))
    logging.info('%s', d.get('y'))

    del c
    del a
    logging.info('%s', d.get('x'))  # should be None
    logging.info('%s', d.get('y'))  # also None
