from itertools import repeat


for i in repeat('over-and-over', 5):
    print(i)


for i in zip(range(7), repeat('over-and-over')):
    print(i)

