import logging
import logging.config

import yaml

with open(file='logging.yaml', mode='r', encoding='utf-8') as f:
    logging_yaml = yaml.load(stream=f, Loader=yaml.FullLoader)
    logging.config.dictConfig(config=logging_yaml)

logger = logging.getLogger('simpleExample')

if __name__ == '__main__':
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')
