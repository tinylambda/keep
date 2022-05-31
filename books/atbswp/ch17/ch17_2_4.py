import logging
import sys

from PIL import Image

logging.basicConfig(level=logging.INFO, stream=sys.stderr)


if __name__ == "__main__":
    cat_image: Image.Image = Image.open("cat.jpeg")
    width, height = cat_image.size

    image_half: Image.Image = cat_image.resize((width // 2, height // 2))
    image_half.save("half.png")

    image_higher: Image.Image = cat_image.resize((width, height + 300))
    image_higher.save("higher.png")
