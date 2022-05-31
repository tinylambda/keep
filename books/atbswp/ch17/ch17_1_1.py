import logging
import pprint
import sys

from PIL import ImageColor

logging.basicConfig(level=logging.INFO, stream=sys.stderr)

if __name__ == "__main__":
    logging.info("show colors: ")
    logging.info(ImageColor.getcolor("red", "RGBA"))
    logging.info(ImageColor.getcolor("RED", "RGBA"))
    logging.info(ImageColor.getcolor("Black", "RGBA"))
    logging.info(ImageColor.getcolor("chocolate", "RGBA"))
    logging.info(ImageColor.getcolor("cornflowerblue", "RGBA"))

    try:
        logging.info(ImageColor.getcolor("notexists", "RGBA"))
    except ValueError as e:
        logging.error("color not exists", e)

    logging.info("show all known colors")
    pprint.pprint(ImageColor.colormap)
