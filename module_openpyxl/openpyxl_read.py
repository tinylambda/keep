import openpyxl


if __name__ == '__main__':
    xlsx_file = '/home/felix/PycharmProjects/document/配置表/character_detail-统帅基础.xlsx'
    wb = openpyxl.load_workbook(xlsx_file)
    sheet = wb.get_sheet_by_name('character_detail')
    config_data = {}

    for row in sheet:
        for c in row:
            print(c.value)

