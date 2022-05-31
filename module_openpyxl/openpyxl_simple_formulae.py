from openpyxl import load_workbook
from openpyxl.utils import FORMULAE


if __name__ == "__main__":
    print(FORMULAE)
    workbook = load_workbook(filename="/Users/felix/Downloads/reviews-sample.xlsx")
    sheet = workbook.active
    sheet["P2"] = "=AVERAGE(H2:H100)"
    sheet["P3"] = '=COUNTIF(I2:I100, ">0")'
    workbook.save(filename="/Users/felix/Downloads/reviews-sample-formulae.xlsx")
