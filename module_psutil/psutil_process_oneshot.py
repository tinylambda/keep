import logging
import sys

import psutil

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == "__main__":
    p = psutil.Process()
    with p.oneshot():
        logging.info(p.name())
        logging.info(p.cpu_times())
        logging.info(p.cpu_percent())
        logging.info(p.create_time())
        logging.info(p.exe())
        logging.info(p.cmdline())
        logging.info(p.environ())
        logging.info(p.as_dict())
        logging.info(p.parent())
        logging.info(p.ppid())
        logging.info(p.cwd())
        logging.info(p.username())
        logging.info(p.uids())
        logging.info(p.gids())
        logging.info(p.terminal())
        logging.info(p.nice())
