import logging
import os
import sys

import psutil

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == "__main__":
    p = psutil.Process()
    logging.info("p.pid = %s; os.getpid = %s", p.pid, os.getpid())

    logging.info("num_fds = %s", p.num_fds())
    for open_file in p.open_files():
        logging.info("opened file = %s", open_file)

    f = open("/tmp/a.txt", "w")
    logging.info("num_fds = %s", p.num_fds())

    logging.info("Before close")
    for open_file in p.open_files():
        logging.info("opened file = %s", open_file)

    f.close()
    logging.info("After close")
    for open_file in p.open_files():
        logging.info("opened file = %s", open_file)
