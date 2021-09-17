import os
import os.path

from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.jpeg'


if __name__ == '__main__':
    logo_image: Image.Image = Image.open(LOGO_FILENAME)
    logo_width, log_height = logo_image.size
    logo_image.resize((100, 100))

    for root, dirs, files in os.walk('.'):
        for file in files:
            name, ext = os.path.splitext(file)
            if ext != '.png' or file == LOGO_FILENAME:
                continue
            png_path = os.path.join(root, file)
            image: Image.Image = Image.open(png_path)
            image_width, image_height = image.size
            print(png_path, image_width, image_height)

            if image_width > SQUARE_FIT_SIZE and image_height > SQUARE_FIT_SIZE:
                if image_width > image_height:
                    image_height = int((SQUARE_FIT_SIZE / image_width) * image_height)
                    image_width = SQUARE_FIT_SIZE
                else:
                    image_width = int((SQUARE_FIT_SIZE / image_height) * image_width)
                    image_height = SQUARE_FIT_SIZE
            print(f'resizing {png_path}...')
            image = image.resize((image_width, image_height))

            print(f'adding logo to {png_path}')
            image.paste(logo_image, (image_width - logo_width, image_height - log_height))
            new_filename = os.path.join('/home/felix/Downloads/images', f'with_logo_{file}')
            image.save(new_filename)
