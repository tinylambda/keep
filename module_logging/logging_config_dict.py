import logging
import logging.config

import yaml

with open(file="logging.yaml", mode="r", encoding="utf-8") as f:
    logging_yaml = yaml.load(stream=f, Loader=yaml.FullLoader)
    logging.config.dictConfig(config=logging_yaml)


class LogProxy:
    def __init__(self, logtype):
        self.logger = logging.getLogger(logtype)

    def record_role(self, role):
        self.logger.info("role is %s", role, stacklevel=2)


if __name__ == "__main__":
    logger = logging.getLogger("simpleExample")
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warn message")
    logger.error("error message")
    logger.critical("critical message")
