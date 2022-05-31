import logging
import sys

from PIL import Image

logging.basicConfig(level=logging.INFO, stream=sys.stderr)


if __name__ == "__main__":
    cat_image: Image.Image = Image.open("cat.jpeg")
    cat_width, cat_height = cat_image.size
    cropped_image: Image.Image = cat_image.crop((335, 345, 565, 560))
    face_width, face_height = cropped_image.size
    copied_image = cat_image.copy()

    for left in range(0, cat_width, face_width):
        for top in range(0, cat_height, face_height):
            logging.info("left: %s, top: %s", left, top)
            copied_image.paste(cropped_image, (left, top))

    copied_image.save("tiled.png")
