import itertools


def count(n):
    while True:
        yield n
        n += 1


c = count(0)
# c[10:20]  # not works

for x in itertools.islice(c, 10, 20):
    print(x)
