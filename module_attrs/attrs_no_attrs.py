import logging
import sys

import attr


logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class Empty:
    pass


if __name__ == '__main__':
    logging.info('%s', Empty())
    logging.info('%s', Empty() == Empty())  # True
    logging.info('%s', Empty() is Empty())  # False
