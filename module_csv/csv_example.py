import csv

import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

if __name__ == '__main__':
    overflow_users = 0
    num = 0

    with open('example.csv') as f:
        csv_file = csv.DictReader(f)
        for row in csv_file:
            num += 1
            distinct_user = int(row.get('distinct_user'))
            overflow_users += distinct_user

    logging.info('%s - %s = %s', overflow_users, num, overflow_users - num)
