import logging
import sys

import psutil

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == "__main__":
    p = psutil.Process()

    with open("/tmp/a.txt", "w") as af, open("/tmp/b.txt", "w") as bf:
        for open_file in p.open_files():
            logging.info("%s", open_file)
