from openpyxl import load_workbook


if __name__ == '__main__':
    workbook = load_workbook('/Users/felix/Downloads/sample.xlsx')
    print(workbook.sheetnames)

    sheet = workbook.active
    print(sheet, sheet.title)

    print(sheet['A1'])
    print(sheet['A1'].value)
    print(sheet['F10'].value)

    print(sheet.cell(row=10, column=6))
    print(sheet.cell(row=10, column=6).value)

