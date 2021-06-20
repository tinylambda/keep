from openpyxl import Workbook


def print_rows():
    for row in sheet.iter_rows(values_only=True):
        print(row)


if __name__ == '__main__':
    filename = '/Users/felix/Downloads/hello_world.xlsx'
    workbook = Workbook()
    sheet = workbook.active
    
    cell = sheet['A1']
    print(cell)
    print(cell.value)
    cell.value = 'hey'
    print(cell.value)
    
    workbook.save(filename=filename)

    print('-' * 64)
    print_rows()

    print('-' * 64)
    sheet['B10'] = 'test'
    print_rows()

    print('-' * 64)
    sheet.insert_cols(idx=1)
    print_rows()

    print('-' * 64)
    sheet.insert_cols(idx=3, amount=5)
    print_rows()

    print('-' * 64)
    sheet.delete_cols(idx=3, amount=5)
    print_rows()

    print('-' * 64)
    sheet.delete_cols(idx=1)
    print_rows()

    print('-' * 64)
    sheet.insert_rows(idx=1)
    print_rows()

    print('-' * 64)
    sheet.insert_rows(idx=1, amount=3)
    print_rows()

    print('-' * 64)
    sheet.delete_rows(idx=1, amount=4)
    print_rows()

