import csv


if __name__ == "__main__":
    f = "/Users/felix/Result_7.csv"
    with open(f) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print("_".join(row[:3]))
