import pathlib

import qrcode
from qrcode.image.pil import PilImage

if __name__ == '__main__':
    img: PilImage = qrcode.make('https://www.baidu.com')
    img.save(pathlib.Path.home().joinpath('Downloads/test.png'))
