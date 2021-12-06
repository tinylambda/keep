import logging
import sys

import yaml

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


class Monster(yaml.YAMLObject):
    yaml_tag = '!Monster'

    def __init__(self, name, hp, ac, attacks):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.attacks = attacks

    def __repr__(self):
        return "%s(name=%r, hp=%r, ac=%r, attacks=%r)" \
               % (self.__class__.__name__, self.name, self.hp, self.ac, self.attacks)


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
hp:
- 2
- 6
name: Cave Spider'''
    result = yaml.unsafe_load(stream)
    logging.info('%s', result)
