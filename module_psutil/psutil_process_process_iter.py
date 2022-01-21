import logging
import sys

import psutil

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        print(proc.info)

    procs = {p.pid: p.info for p in psutil.process_iter(['name', 'username'])}
    logging.info('%s', procs)
