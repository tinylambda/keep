import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class User:
    email = attr.ib(
        validator=attr.validators.matches_re('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'))


if __name__ == '__main__':
    user = User(email='user@example.com')
    logging.info('%s', user)

    user = User(email='user@example.com@test.com')  # should raise Value error
