import pathlib

from openpyxl import Workbook
from openpyxl.styles import NamedStyle, Font, Border, Side, Alignment

if __name__ == "__main__":
    header = NamedStyle(name="header")
    header.font = Font(bold=True)
    header.border = Border(bottom=Side(border_style="thin"))
    header.alignment = Alignment(horizontal="center", vertical="center")

    workbook = Workbook()
    sheet = workbook.create_sheet("Sample Sheet")
    sheet.append(("this", "is", "a", "good", "thing"))
    header_row = sheet[1]
    for cell in header_row:
        cell.style = header

    filepath = pathlib.Path.home().joinpath("Downloads/test2.xlsx")
    workbook.save(filepath)
