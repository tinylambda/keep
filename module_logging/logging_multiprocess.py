import concurrent.futures
import logging
import logging.handlers
import sys


def do_log(n):
    logger = logging.getLogger()
    handler = logging.StreamHandler(stream=sys.stdout)
    formatter = logging.Formatter(
        r"%(asctime)s %(name)s[%(process)d] [%(levelname)s] %(message)s"
    )
    handler.setFormatter(formatter)
    handler.setLevel(logging.DEBUG)
    logger.handlers = [handler]
    logger.setLevel(logging.DEBUG)

    for i in range(1000):
        logger.info("Hi %s", i)


if __name__ == "__main__":
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=16)
    results = executor.map(do_log, range(16))
