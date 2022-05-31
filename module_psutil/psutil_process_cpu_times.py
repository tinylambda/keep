import logging
import sys

import psutil

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == "__main__":
    p = psutil.Process()

    cpu_times = p.cpu_times()
    logging.info("cpu times = %s", cpu_times)
    logging.info("cumulative, excluding children and iowait = %s", sum(cpu_times[:2]))
