import logging
import sys

import attr

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class LoginInfo:
    recent_login_days = attr.ib(type=set)


@attr.s
class User:
    login_info = attr.ib(type=LoginInfo)


if __name__ == "__main__":
    user = User(LoginInfo({"20210901", "20210902", "20210903"}))
    logging.info("%s", attr.asdict(user, recurse=True, retain_collection_types=False))
    logging.info("%s", attr.asdict(user, recurse=True, retain_collection_types=True))
