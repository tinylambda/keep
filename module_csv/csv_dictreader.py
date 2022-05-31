import csv
import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

if __name__ == "__main__":
    with open(sys.argv[1], "rt") as f:
        reader = csv.DictReader(f)
        for row in reader:
            logging.info("%s", row)
# python module_csv/csv_dictreader.py module_csv/example.csv
