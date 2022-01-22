import logging
import sys
from subprocess import PIPE

import psutil

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    p = psutil.Popen(['python', '-c', 'print("hello world")'], stdout=PIPE)
    logging.info('p.name = %s', p.name())
    logging.info('p.username = %s', p.username())
    logging.info('p.communicate = %s', p.communicate())

    try:
        p = psutil.Popen(['sleep', '3'], stdout=PIPE)
        p.wait(timeout=2)
    except psutil.TimeoutExpired:
        logging.info('timeout works')
