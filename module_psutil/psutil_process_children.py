import logging
import sys

import psutil

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == "__main__":
    p = psutil.Process(pid=1)

    for process in p.children(recursive=False):
        logging.info("%s", process)
