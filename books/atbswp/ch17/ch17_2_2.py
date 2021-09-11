import logging
import sys

from PIL import Image

logging.basicConfig(level=logging.INFO, stream=sys.stderr)


if __name__ == '__main__':
    cat_image: Image.Image = Image.open('cat.jpeg')
    logging.info(cat_image.size)
    width, height = cat_image.size
    logging.info('width is %s and height is %s', width, height)
    logging.info('filename is %s', cat_image.filename)
    logging.info('file format is %s', cat_image.format)
    logging.info('file format description is %s', cat_image.format_description)
    cat_image.save('cat.png')

    cat_image_png: Image.Image = Image.open('cat.png')
    logging.info('file format description is %s', cat_image_png.format_description)

    # create a blank image
    blank_image = Image.new('RGBA', (200, 200), 'purple')
    blank_image.save('blank.png')
    blank_image_2 = Image.new('RGBA', (20, 20))
    blank_image_2.save('blank2.png')
