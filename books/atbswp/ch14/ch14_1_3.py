import csv


if __name__ == "__main__":
    csv_output_path = "/home/felix/Downloads/test_write.csv"
    csv_output = open(csv_output_path, "w")
    csv_writer = csv.writer(csv_output)
    csv_writer.writerow(["1", "2", "3"])
    csv_writer.writerow(["a", "b", "c"])
    csv_writer.writerow(["Hello, world", "this is good", "fork me"])

    csv_output.close()
