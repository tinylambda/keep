import pathlib
from openpyxl.workbook import Workbook
from openpyxl.styles import Font, Color, Alignment, Border, Side


if __name__ == '__main__':
    bold_font = Font(bold=True)
    big_red_text = Font(color='00FF0000', size=20)
    center_aligned_text = Alignment(horizontal='center')
    double_border_side = Side(border_style='double')
    square_border = Border(top=double_border_side, right=double_border_side,
                           bottom=double_border_side, left=double_border_side)

    workbook = Workbook()
    sheet = workbook.create_sheet('Sample Sheet')

    sheet['A2'] = 'test'
    sheet['A3'] = 'test'
    sheet['A4'] = 'test'
    sheet['A5'] = 'test'

    sheet['A2'].font = bold_font
    sheet['A3'].font = big_red_text
    sheet['A4'].alignment = center_aligned_text
    sheet['A5'].border = square_border

    sheet['A6'] = 'apply multiple styles'
    sheet['A6'].alignment = center_aligned_text
    sheet['A6'].font = big_red_text
    sheet['A6'].border = square_border

    filepath = pathlib.Path.home().joinpath('Downloads/test.xlsx')
    workbook.save(filepath)
