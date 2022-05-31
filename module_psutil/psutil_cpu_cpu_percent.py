import logging
import pprint
import sys

import psutil

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


if __name__ == "__main__":
    logging.info("interval = 1 (blocking)")
    pprint.pprint(psutil.cpu_percent(interval=1))

    logging.info("interval = None (non-blocking, percentage since last call)")
    pprint.pprint(psutil.cpu_percent(interval=None))

    logging.info("interval = 1 and percpu = True")
    pprint.pprint(psutil.cpu_percent(interval=1, percpu=True))
