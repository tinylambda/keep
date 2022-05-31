import logging
import sys

import psutil
import requests

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == "__main__":
    p = psutil.Process()

    with requests.Session() as session:
        session.get("https://www.baidu.com/")

        for connection in p.connections():
            logging.info("%s", connection)
