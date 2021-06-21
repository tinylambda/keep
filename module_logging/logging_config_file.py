import logging
import logging.config

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('simpleExample')

if __name__ == '__main__':
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')

