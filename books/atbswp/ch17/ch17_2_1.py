import logging
import sys

from PIL import Image

logging.basicConfig(level=logging.INFO, stream=sys.stderr)


if __name__ == "__main__":
    cat_image = Image.open("cat.jpeg")
    logging.info(cat_image)
