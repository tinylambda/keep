import pathlib

from openpyxl import Workbook
from openpyxl.formatting.rule import ColorScaleRule

if __name__ == '__main__':
    color_scale_rule = ColorScaleRule(start_type='min', start_color='00FF0000', end_type='max', end_color='0000FF00')
    workbook = Workbook()
    sheet = workbook.create_sheet('Sample Sheet')
    sheet.append((1, 2, 3))
    sheet.append((1, 2, 3))
    sheet.append((-1, 2, 3))
    sheet.append((-2, 2, 3))
    sheet.append((-2, 2, 3))
    sheet.append((2, 2, 3))

    sheet.conditional_formatting.add('A2:A10', color_scale_rule)

    filepath = pathlib.Path.home().joinpath('Downloads/test4.xlsx')
    workbook.save(filepath)

