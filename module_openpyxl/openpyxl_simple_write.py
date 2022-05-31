from openpyxl import Workbook


if __name__ == "__main__":
    workbook = Workbook()
    sheet = workbook.active

    sheet["A1"] = "hello"
    sheet["B1"] = "world!"

    workbook.save(filename="/Users/felix/Downloads/hello_world.xlsx")
