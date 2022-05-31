from module_logging.logging_config_dict import LogProxy


if __name__ == "__main__":
    lp = LogProxy("mytestlogger")
    lp.record_role("felix")

    logger = lp.logger
    logger.info("felix 2")
