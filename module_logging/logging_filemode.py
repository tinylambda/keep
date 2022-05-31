import logging


logging.basicConfig(
    filename="/tmp/example.log",
    encoding="utf-8",
    level=logging.DEBUG,
    filemode="w",
)


if __name__ == "__main__":
    logging.debug("This message should go to the log file")
    logging.info("So should this")
    logging.warning("And this, too")
    logging.error("And non-ASCII stull, too, like 你好 and 。")
