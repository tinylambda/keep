from openpyxl import load_workbook


if __name__ == '__main__':
    workbook = load_workbook(filename='/Users/felix/Downloads/hello_world.xlsx')
    sheet = workbook.active

    sheet['C1'] = 'writing ;)'
    workbook.save(filename='/Users/felix/Downloads/hello_world_append.xlsx')

