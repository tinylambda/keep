import logging
import sys

import yaml

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    result = yaml.load("""
    - Hesperiidae
    - Papilionidae
    - Apatelodidae
    - Epiplemidae
    """, yaml.SafeLoader)
    logging.info('%s', result)
