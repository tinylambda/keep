import logging
from pprint import pformat

from module_pprint.pprint_data import data

logging.basicConfig(level=logging.DEBUG, format='%(levelname)-8s %(message)s')

if __name__ == '__main__':
    logging.debug('Logging pformatted data')
    formatted = pformat(data)
    for line in formatted.splitlines():
        logging.debug('%s', line.rstrip())
