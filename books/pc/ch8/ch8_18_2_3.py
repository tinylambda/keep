from ch8_18_2 import *
from collections import OrderedDict


class StringOrderedDict(StringKeysMappingMixin, SetOnceMixin, OrderedDict):
    pass


if __name__ == '__main__':
    d = StringOrderedDict()
    d['x'] = 23
    try:
        d[42] = 10
    except TypeError as e:
        logger.exception(e)

    try:
        d['x'] = 42
    except KeyError as e:
        logger.exception(e)

