import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


class SomethingFromSomeoneElse:
    def __init__(self, x):
        self.x = x


SomethingFromSomeoneElse = attr.s(these={'x': attr.ib()}, init=False)(SomethingFromSomeoneElse)


if __name__ == '__main__':
    logging.info('%s', SomethingFromSomeoneElse(1))
