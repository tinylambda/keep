import logging
import pprint
import sys

import psutil

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    pprint.pprint(psutil.cpu_stats())
