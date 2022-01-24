import logging
import logging.handlers
import sys


if __name__ == '__main__':
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setLevel(logging.DEBUG)

    LOG_FMT = r"%(asctime)s %(name)s[%(process)d] [%(levelname)s] %(message)s"
    LOG_DATE_FMT = r"%Y-%m-%d %H:%M:%S"

    formatter = logging.Formatter(fmt=LOG_FMT, datefmt=LOG_DATE_FMT)
    handler.setFormatter(formatter)
    root_logger.handlers = [handler]

    root_logger.info('GOOD')
    logging.getLogger().info('GOOD')

    logging.getLogger('circus').info('GOOD')



