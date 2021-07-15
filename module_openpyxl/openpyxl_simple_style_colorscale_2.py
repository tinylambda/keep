import pathlib

from openpyxl import Workbook
from openpyxl.formatting.rule import ColorScaleRule


if __name__ == '__main__':
    color_scale_rule = ColorScaleRule(
        start_type='num',
        start_value=1,
        start_color='00FF0000',
        mid_type='num',
        mid_value=3,
        mid_color='00FFFF00',
        end_type='num',
        end_value=5,
        end_color='0000FF00',
    )

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

    sheet.conditional_formatting.add('A2:A10', color_scale_rule)

    filepath = pathlib.Path.home().joinpath('Downloads/test5.xlsx')
    workbook.save(filepath)

