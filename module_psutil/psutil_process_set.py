import logging
import sys

import psutil

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    p = psutil.Process()
    logging.info(p.pid)
    if psutil.LINUX:
        p.ionice(psutil.IOPRIO_CLASS_RT, value=7)
    else:
        p.ionice(psutil.IOPRIO_HIGH)

    logging.info(p.ionice())
