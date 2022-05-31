import csv

import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


with open(sys.argv[1], "rt", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        logging.info("%s", row)

# python module_csv/csv_reader.py module_csv/example.csv
