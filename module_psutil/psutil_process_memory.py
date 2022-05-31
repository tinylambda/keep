import logging
import sys
import time

import psutil

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == "__main__":
    p = psutil.Process()
    logging.info("memory info: %s", p.memory_info())
    logging.info("memory full info: %s", p.memory_full_info())

    # this is the non-swapped physical memory a process has used
    logging.info("memory percent rss: %s", p.memory_percent("rss"))

    # the memory which is unique to a process and which would be freed if the process was terminated right now
    logging.info("memory percent uss: %s", p.memory_percent("uss"))

    # the amount of memory shared with other processes, accounted in a way that the amount is divided evenly between the
    # processes that share it. I.e. if a process has 10 MBs all to itself and 10 MBs shared with another process
    # its PSS will be 15 MBs.
    logging.info("memory percent pss: %s", p.memory_percent("pss"))

    # memory that could be potentially shared with other processes. This matches “top“‘s SHR column
    logging.info("memory percent shared: %s", p.memory_percent("shared"))

    # aka “Virtual Memory Size”, this is the total amount of virtual memory used by the process
    logging.info("memory percent vms: %s", p.memory_percent("vms"))

    # Return process’s mapped memory regions as a list of named tuples
    # whose fields are variable depending on the platform
    for memory_map in p.memory_maps():
        logging.info("memory maps: %s", memory_map)

    # sleep some time to take a look at the output of top or htop of this process
    logging.info("PID = %s", p.pid)
    time.sleep(100)
