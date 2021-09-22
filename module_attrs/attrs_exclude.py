import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    user = attr.ib()
    password = attr.ib(repr=False)


@attr.s
class D:
    user = attr.ib()
    password = attr.ib(repr=lambda value: '***')


if __name__ == '__main__':
    c = C('me', 's3kr3t')
    logging.info('%s', c)

    d = D('felix', '324hgkd')
    logging.info('%s', d)
