import csv

from collections import namedtuple


if __name__ == "__main__":
    with open("stock.csv") as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        print(headers)
        for row in f_csv:
            print(row)

    with open("stock.csv") as f:
        f_csv = csv.reader(f)
        headings = next(f_csv)
        Row = namedtuple("Row", headings)
        for r in f_csv:
            row = Row(*r)
            print(row)

    with open("stock.csv") as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            print(row)

    headers = ["A", "B", "C"]
    rows = [
        (1, 2, 3),
        (10, 20, 30),
        (100, 200, 300),
    ]

    with open("/tmp/test.csv", "w") as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)

    headers = ["D", "E", "F"]
    rows = [
        {"D": 11, "E": 22, "F": 33},
        {"D": 111, "E": 222, "F": 333},
        {"D": 1111, "E": 2222, "F": 3333},
    ]

    with open("/tmp/test2.csv", "w") as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()
        f_csv.writerows(rows)
