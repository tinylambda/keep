import logging
import pprint
import sys

import psutil

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


if __name__ == "__main__":
    # The “load” represents the processes which are in a runnable state,
    # either using the CPU or waiting to use the CPU (e.g. waiting for disk I/O).

    logging.info("Default")
    pprint.pprint(psutil.getloadavg())

    cpu_count = psutil.cpu_count(logical=True)
    pprint.pprint([x / cpu_count * 100 for x in psutil.getloadavg()])
