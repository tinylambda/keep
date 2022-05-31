import logging
import sys

import psutil

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == "__main__":
    p = psutil.Process()
    logging.info(
        "CPU num (Return what CPU this process is currently running on) = %s",
        p.cpu_num(),
    )
