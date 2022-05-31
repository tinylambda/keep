import logging
import sys

import psutil

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == "__main__":
    p = psutil.Process()
    logging.info("%s (%s)", p.name(), p.pid)
    logging.info("%s", p.io_counters())
