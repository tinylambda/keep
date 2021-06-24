from openpyxl import load_workbook

if __name__ == '__main__':
    workbook = load_workbook(filename='/Users/felix/Downloads/reviews-sample.xlsx')
    sheet = workbook.active
    print(sheet.dimensions)
    sheet.auto_filter.ref = 'A1:O100'
    workbook.save(filename='/Users/felix/Downloads/reviews-sample-with-filters.xlsx')

