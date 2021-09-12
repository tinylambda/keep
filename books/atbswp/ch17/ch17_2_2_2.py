import logging
import sys

from PIL import Image

logging.basicConfig(level=logging.INFO, stream=sys.stderr)


if __name__ == '__main__':
    cat_image: Image.Image = Image.open('cat.jpeg')
    cropped_image: Image.Image = cat_image.crop((335, 345, 565, 560))
    cropped_image.save('cropped.png')
