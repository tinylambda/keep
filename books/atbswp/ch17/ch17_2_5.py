import logging
import sys

from PIL import Image

logging.basicConfig(level=logging.INFO, stream=sys.stderr)


if __name__ == "__main__":
    cat_image: Image.Image = Image.open("cat.jpeg")
    cat_image.rotate(90).save("rotate90.png")
    cat_image.rotate(180).save("rotate180.png")
    cat_image.rotate(270).save("rotate270.png")

    # use expand
    cat_image.rotate(6).save("rotate6.png")
    cat_image.rotate(6, expand=True).save("rotate6_expanded.png")

    # mirror rotate
    cat_image.transpose(Image.FLIP_LEFT_RIGHT).save("horizontal_flip.png")
    cat_image.transpose(Image.FLIP_TOP_BOTTOM).save("vertical_flip.png")
