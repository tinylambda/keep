import csv

import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

csv.register_dialect('pipes', delimiter='|')

with open('example.pipes', 'r') as f:
    reader = csv.reader(f, dialect='pipes')
    for row in reader:
        logging.info('%s', row)
