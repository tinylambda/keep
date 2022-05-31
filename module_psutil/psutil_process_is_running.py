import logging
import sys

import psutil

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == "__main__":
    p = psutil.Process()

    if p.status() == psutil.STATUS_ZOMBIE:
        logging.info("ZOMBIE process!")

    logging.info("Process is_running? = %s", p.is_running())
