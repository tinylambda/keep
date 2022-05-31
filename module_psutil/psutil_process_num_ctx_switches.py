import logging
import sys
import time

import psutil

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == "__main__":
    p = psutil.Process()
    time.sleep(1)  # voluntary switch by sleep
    logging.info("%s", p.num_ctx_switches())
    logging.info("%s", p.num_ctx_switches())
    time.sleep(1)
    logging.info("%s", p.num_ctx_switches())
