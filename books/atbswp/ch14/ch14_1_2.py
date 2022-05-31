import csv


if __name__ == "__main__":
    csv_file_path = "/home/felix/Downloads/test.csv"
    csv_file = open(csv_file_path, "rt")
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(f"{csv_reader.line_num}: {row}")
