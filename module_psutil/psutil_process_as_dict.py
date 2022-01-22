import logging
import pprint
import sys

import psutil

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


if __name__ == '__main__':
    p = psutil.Process()

    logging.info('Default')
    pprint.pprint(p.as_dict())
