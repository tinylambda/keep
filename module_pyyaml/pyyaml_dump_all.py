import logging
import sys

import yaml

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    result = yaml.dump([1, 2, 3], explicit_start=True)
    logging.info('%s', result)

    result = yaml.dump_all([1, 2, 3], explicit_start=True)
    logging.info('%s', result)
