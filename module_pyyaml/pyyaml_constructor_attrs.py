import logging
import sys

import attr
import yaml

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


@attr.s
class Monster(yaml.YAMLObject):
    yaml_tag = '!Monster'

    name = attr.ib()
    hp = attr.ib()
    ac = attr.ib()
    attacks = attr.ib()


if __name__ == '__main__':
    monster = Monster('Cave Spider', [2, 6], 16, ['BITE', "HURT"])
    result = yaml.dump(monster, explicit_start=True, default_flow_style=True)
    logging.info('%s', result)

    result = yaml.dump(monster, explicit_start=True, default_flow_style=False)
    logging.info('%s', result)

    stream = '''!Monster
ac: 16
attacks:
- BITE
- HURT
hp: [2, 6]
name: Cave Spider'''
    result = yaml.unsafe_load(stream)
    logging.info('%s', result)
