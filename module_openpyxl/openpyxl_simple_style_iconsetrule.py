import pathlib

from openpyxl import Workbook
from openpyxl.formatting.rule import IconSetRule


if __name__ == '__main__':
    icon_set_rule = IconSetRule(
        "5Arrows",
        "num",
        [1, 2, 3, 4, 5]
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

    sheet.conditional_formatting.add('A2:A10', icon_set_rule)

    filepath = pathlib.Path.home().joinpath('Downloads/test6.xlsx')
    workbook.save(filepath)

