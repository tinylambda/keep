import logging
import pprint
import sys

import psutil

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


if __name__ == '__main__':
    logging.info('Default')
    pprint.pprint(psutil.cpu_count())

    logging.info('logical = False')
    pprint.pprint(psutil.cpu_count(logical=False))

    logging.info('The number of usable CPUs can be obtained is %s', psutil.Process().cpu_affinity())
