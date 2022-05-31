import logging
import pprint
import sys

import psutil

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


if __name__ == "__main__":
    logging.info("default: ")
    pprint.pprint(psutil.net_io_counters())

    logging.info("pernic = True: ")
    pprint.pprint(psutil.net_io_counters(pernic=True))
