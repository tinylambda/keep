import logging
import pprint
import sys

import psutil

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


if __name__ == '__main__':
    logging.info('Default')
    pprint.pprint(psutil.cpu_freq())

    logging.info('percpu = True')
    pprint.pprint(psutil.cpu_freq(percpu=True))
