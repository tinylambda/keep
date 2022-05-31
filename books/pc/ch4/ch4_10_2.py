from collections import defaultdict


my_list = ["a", "b", "c"]

for idx, val in enumerate(my_list):
    print(idx, val)

print("-" * 64)

for idx, val in enumerate(my_list, 1):
    print(idx, val)


def parse_data(filename):
    with open(filename, "rt") as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(fields[0])
            except ValueError as e:
                print("line {}: parse error: {}".format(lineno, e))


parse_data("test.txt")

print("-" * 64)


word_summary = defaultdict(list)

with open("ch4_6_3.py", "r") as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)

print(word_summary)

print("-" * 64)

data = [(1, 2), (3, 4), (5, 6), (7, 8)]
for n, (x, y) in enumerate(data):
    print(n, x, y)


for item in enumerate(data):
    print(item)
