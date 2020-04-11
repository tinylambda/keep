from itertools import cycle

for i in zip(range(7), cycle(['a', 'b', 'c'])):
    print(i)

# for item in cycle(['a', 'b', 'c']):
#     print(item)

