import logging
import sys

import psutil

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == "__main__":
    p = psutil.Process()
    p.rlimit(psutil.RLIMIT_NOFILE, (128, 128))
    p.rlimit(psutil.RLIMIT_FSIZE, (1024, 1024))

    logging.info(p.rlimit(psutil.RLIMIT_FSIZE))
