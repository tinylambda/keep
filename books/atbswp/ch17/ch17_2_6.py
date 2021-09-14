import logging
import sys

from PIL import Image, ImageColor

logging.basicConfig(level=logging.INFO, stream=sys.stderr)


if __name__ == '__main__':
    image: Image.Image = Image.new('RGBA', (100, 100))
    logging.info('%s', image.getpixel((0, 0)))

    my_color = (210, 210, 210)
    darkgray_color = ImageColor.getcolor('darkgrey', 'RGBA')

    for x in range(100):
        for y in range(50):
            image.putpixel((x, y), my_color)

    for x in range(100):
        for y in range(50, 100):
            image.putpixel((x, y), darkgray_color)

    logging.info('%s', image.getpixel((0, 0)))
    logging.info('%s', image.getpixel((0, 50)))

    image.save('put_pixel.png')
