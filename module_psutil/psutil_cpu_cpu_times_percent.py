import logging
import pprint
import sys

import psutil

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


if __name__ == '__main__':
    logging.info('Default')
    pprint.pprint(psutil.cpu_times_percent())

    logging.info('interval = 1')
    pprint.pprint(psutil.cpu_times_percent(interval=1))

    logging.info('interval = 1 and percpu = True')
    pprint.pprint(psutil.cpu_times_percent(interval=1, percpu=True))
