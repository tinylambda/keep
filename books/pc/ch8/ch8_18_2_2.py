from ch8_18_2 import *
from collections import defaultdict


class SetOnceDefaultDict(SetOnceMixin, defaultdict):
    pass


if __name__ == '__main__':
    d = SetOnceDefaultDict(list)
    d['x'].append(2)
    d['x'].append(3)
    d['x'].append(10)
    try:
        d['x'] = 30
    except KeyError as e:
        logger.exception(e)

