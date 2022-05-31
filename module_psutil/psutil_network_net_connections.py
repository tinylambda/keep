import logging
import sys

import psutil

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == "__main__":
    for net_connection in psutil.net_connections():
        logging.info("net_connection = %s", net_connection)
