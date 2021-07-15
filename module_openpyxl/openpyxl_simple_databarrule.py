import pathlib

from openpyxl import Workbook
from openpyxl.formatting.rule import DataBarRule


if __name__ == '__main__':
    data_bar_rule = DataBarRule(
        start_type='num',
        start_value=1,
        end_type='num',
        end_value=5,
        color='0000FF00'
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

    sheet.conditional_formatting.add('A2:A10', data_bar_rule)

    filepath = pathlib.Path.home().joinpath('Downloads/test7.xlsx')
    workbook.save(filepath)

