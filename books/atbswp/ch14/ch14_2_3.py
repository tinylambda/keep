import csv


if __name__ == '__main__':
    csv_empty_path = '/home/felix/Downloads/empty.csv'
    csv_file_path = '/home/felix/Downloads/test.csv'
    # csv_file = open(csv_empty_path, 'rt')
    csv_file = open(csv_file_path, 'rt')
    csv_reader = csv.reader(csv_file)

    try:
        first_line = next(csv_reader)
    except StopIteration:
        first_line = None

    if first_line is None:
        raise SystemExit()
    print(f'header: {first_line}')

    for row in csv_reader:
        print(f'{csv_reader.line_num}: {row}')
