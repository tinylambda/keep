import logging
import mylib


def main():
    logging.basicConfig(filename="/tmp/myapp.log", level=logging.INFO)
    logging.info("Started")
    mylib.do_something()
    logging.info("Finished")


if __name__ == "__main__":
    main()
