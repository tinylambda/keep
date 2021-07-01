from itertools import dropwhile, islice


with open('/etc/passwd') as f:
    for line in f:
        print(line, end='')

print('-' * 64)

with open('/etc/passwd') as f:
    for line in dropwhile(lambda line: line.startswith('root'), f):
        print(line, end='')

print('-' * 64)

items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x)

