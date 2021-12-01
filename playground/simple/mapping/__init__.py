import logging
import sys

import yaml

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    tables: dict = yaml.safe_load(open('tables.yaml'))

    for table_name, table_detail in tables.items():
        logging.info('Table: %s', table_name)
        for column in table_detail['columns']:
            logging.info('\t\t%s', column)

    datasets = yaml.safe_load(open('datasets.yaml'))
    logging.info('%s', datasets)
