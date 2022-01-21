import logging
import sys

import psutil

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    logging.info('%s', psutil.pid_exists(1))
    logging.info('%s', psutil.pid_exists(3022))
