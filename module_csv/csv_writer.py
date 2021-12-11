import csv

import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


unicode_chars = '中国人'

with open(sys.argv[1], 'wt', encoding='utf-8') as f:
    # writer = csv.writer(f)
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)  # add quoting for non-numeric data
    writer.writerow(('Title 1', 'Title 2', 'Title 3', 'Title 4'))
    for i in range(3):
        row = (i+1, chr(ord('a') + i), '08/{:02d}/07'.format(i + 1), unicode_chars[i])
        writer.writerow(row)

logging.info('%s', open(sys.argv[1], 'rt').read())

# python module_csv/csv_writer.py /tmp/test.csv
