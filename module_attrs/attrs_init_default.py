import inspect
import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class C:
    a = attr.ib(default=42)
    b = attr.ib(default=attr.Factory(list))
    c = attr.ib(factory=list)
    d = attr.ib()

    @d.default
    def _any_name_except_a_name_of_an_attribute(self):
        return {}


@attr.s
class CWithBadDefault:
    x = attr.ib(default=[])


if __name__ == '__main__':
    c = C()
    logging.info('%s', c)

    bad_one = CWithBadDefault()
    bad_two = CWithBadDefault()
    bad_one.x.append(87)
    logging.info('%s', bad_two.x)
