import datetime
import logging
import sys

import psutil

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    boot_time = psutil.boot_time()

    logging.info('boot_time = %s', psutil.boot_time())
    logging.info('boot_time = %s', datetime.datetime.fromtimestamp(boot_time))

    logging.info('Users currently connected on the system')
    for user in psutil.users():
        logging.info('user = %s', user)
