import logging
import pprint
import sys

import psutil

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


if __name__ == "__main__":
    logging.info("Default")
    pprint.pprint(psutil.disk_partitions())

    logging.info("all = True")
    pprint.pprint(psutil.disk_partitions(all=True))
