import logging
import signal
import sys
import time

import psutil

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    p = psutil.Process()

    logging.info('(pid = %s) is_running? = %s', p.pid, p.is_running())

    try:
        p.send_signal(signal.SIGTERM)
    finally:
        logging.info('is_running after send SIGTERM = %s', p.is_running())
