import csv

import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

if __name__ == '__main__':
    logging.info('%s', csv.list_dialects())
