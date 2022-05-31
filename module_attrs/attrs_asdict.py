import logging
import sys

import attr

from module_attrs.attrs_with_attrs import Coordinates

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class UserList:
    users = attr.ib()


@attr.s
class User:
    email = attr.ib()
    password = attr.ib()


if __name__ == "__main__":
    logging.info("%s", attr.asdict(Coordinates(1, 2)))

    r = attr.asdict(
        UserList(
            [User("hello@world.com", "hello123"), User("good@world.com", "good123")]
        ),
        filter=lambda attribute, value: attribute.name != "password",
    )
    logging.info("%s", r)
