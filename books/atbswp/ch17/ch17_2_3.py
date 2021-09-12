import logging
import sys

from PIL import Image

logging.basicConfig(level=logging.INFO, stream=sys.stderr)


if __name__ == '__main__':
    cat_image: Image.Image = Image.open('cat.jpeg')
    cat_copied: Image.Image = cat_image.copy()
    cropped_image: Image.Image = cat_image.crop((335, 345, 565, 560))
    logging.info('%s', cropped_image.size)

    cat_copied.paste(cropped_image, (0, 0))
    cat_copied.paste(cropped_image, (200, 300))
    cat_copied.save('pasted.png')
