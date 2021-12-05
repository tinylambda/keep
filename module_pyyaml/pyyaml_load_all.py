import logging
import sys

import yaml

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    for data in yaml.load_all(open('documents.yaml'), yaml.SafeLoader):
        logging.info('%s', data)
