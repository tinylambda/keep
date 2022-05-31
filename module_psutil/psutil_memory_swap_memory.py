import logging
import pprint
import sys

import psutil

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == "__main__":
    pprint.pprint(psutil.swap_memory())

    # total: total swap memory in bytes
    # used: used swap memory in bytes
    # free: free swap memory in bytes
    # percent: the percentage usage calculated as (total - available) / total * 100
    # sin: the number of bytes the system has swapped in from disk (cumulative)
    # sout: the number of bytes the system has swapped out from disk (cumulative)
