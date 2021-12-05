import logging
import sys

import yaml

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    result = yaml.load(
        """hello: 中国""", yaml.SafeLoader)
    logging.info('%s', result)
