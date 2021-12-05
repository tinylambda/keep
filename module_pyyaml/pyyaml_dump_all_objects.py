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


if __name__ == '__main__':
    felix = Hero('Felix', hp=1200, sp=0)
    result = yaml.dump(felix)
    logging.info('%s', result)

    fanny = Hero('Fanny', hp=1200000, sp=0)
    result = yaml.dump_all([felix, fanny], explicit_start=True)
    logging.info('%s', result)
