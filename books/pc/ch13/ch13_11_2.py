import logging


def main():
    logging.basicConfig(
        filename="app.log",
        level=logging.WARNING,
    )

    hostname = "www.python.org"
    item = "spam"
    filename = "data.csv"
    mode = "r"

    # example logging calls (insert into your program)
    logging.critical("host %s unknown", hostname)
    logging.error("could not file item %r", item)
    logging.warning("feature is depreciated")
    logging.info("opening file %r mode %r", filename, mode)
    logging.debug("got here")


if __name__ == "__main__":
    main()
