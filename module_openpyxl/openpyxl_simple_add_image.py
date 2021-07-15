import pathlib

from openpyxl import Workbook
from openpyxl.drawing.image import Image


if __name__ == '__main__':
    workbook = Workbook()
    sheet = workbook.create_sheet('Sample Sheet')
    sheet.append((1, 2, 3))
    sheet.append((1, 2, 3))
    sheet.append((-1, 2, 3))
    sheet.append((-2, 2, 3))
    sheet.append((-2, 2, 3))
    sheet.append((2, 2, 3))
    sheet.append((20, 2, 3))
    sheet.append((200, 2, 3))

    logo = Image('real-python.png')
    logo.height = 150
    logo.width = 150
    sheet.add_image(logo, 'B50')

    filepath = pathlib.Path.home().joinpath('Downloads/test8.xlsx')
    workbook.save(filepath)

