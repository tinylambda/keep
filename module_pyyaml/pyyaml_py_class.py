import logging
import sys

import attr
import yaml

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class Hero:
    name = attr.ib()
    hp = attr.ib()
    sp = attr.ib()


if __name__ == "__main__":
    result = yaml.load(
        """
    !!python/object:__main__.Hero
    name: Felix
    hp: 1200
    sp: 0
    """,
        yaml.UnsafeLoader,
    )
    logging.info("%s", result)
