import enum
import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


class State(enum.Enum):
    ON = 'on'
    OFF = 'off'


@attr.s
class C:
    state = attr.ib(validator=attr.validators.in_(State))
    val = attr.ib(validator=attr.validators.in_([1, 2, 3]))


if __name__ == '__main__':
    c = C(State.ON, 1)
    logging.info('%s', c)

    try:
        c = C('on', 1)
    except ValueError as e:
        logging.info('error 1')

    try:
        c = C(State.ON, 4)
    except ValueError as e:
        logging.error('error 2')