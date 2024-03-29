import logging
import sys

import yaml

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


class Dice(tuple):
    def __new__(cls, a, b):
        return tuple.__new__(cls, [a, b])

    def __repr__(self):
        return "Dice(%s, %s)" % self


def dice_representer(dumper, data):
    return dumper.represent_scalar("!dice", "%sd%s" % data)


def dice_constructor(loader, node):
    value = loader.construct_scalar(node)
    a, b = map(int, value.split("d"))
    return Dice(a, b)


yaml.add_representer(Dice, dice_representer)
yaml.add_constructor("!dice", dice_constructor)

if __name__ == "__main__":
    logging.info("%s", Dice(3, 6))
    logging.info("%s", yaml.dump(Dice(3, 6)))
    logging.info("%s", yaml.dump({"gold": Dice(3, 6)}))
    logging.info("%s", yaml.unsafe_load("""initial hit points: !dice 8d4"""))
