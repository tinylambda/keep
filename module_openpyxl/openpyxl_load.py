import openpyxl


if __name__ == "__main__":
    xlsx_file = "/home/felix/PycharmProjects/document/配置表/item-道具.xlsx"
    wb = openpyxl.load_workbook(xlsx_file)
    print(type(wb))
    sheet_names = wb.get_sheet_names()

    for sheet_name in sheet_names:
        print(f"Processing sheet {sheet_name}")
        sheet = wb.get_sheet_by_name(sheet_name)
        print(type(sheet), sheet.title)
