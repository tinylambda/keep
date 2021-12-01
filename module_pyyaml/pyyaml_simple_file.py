import logging
import sys

import yaml

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

if __name__ == '__main__':
    result = yaml.safe_load(open('simple_file.yaml'))
    logging.info('%s', result)
    for item in result:
        logging.info('got table: %s', item)
