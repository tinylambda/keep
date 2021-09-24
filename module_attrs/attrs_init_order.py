import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

"""
If present, the hooks are executed in the following order:
1. __attrs_pre_init__ (if present on current class)
For each attribute, in the order it was declared:
2.1 default factory
2.2 converter
2.3 all validators
3 __attrs_post_init__ (if present on current class)
"""


@attr.s
class C:
    x = attr.ib()
    y = attr.ib(init=False)

    @y.validator
    def _validate_y(self, attribute, value):
        if value < 0:
            raise ValueError('y should be > 0')

    # @x.validator
    # def _validate_y(self, attribute, value):
    #     if value < 0:
    #         raise ValueError('x should be > 0')


if __name__ == '__main__':
    c = C(-3)
    logging.info('%s', c)
