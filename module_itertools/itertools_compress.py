from itertools import cycle, compress


every_third = cycle([False, False, True])
data = range(1, 10)

for i in compress(data, every_third):
    print(i, end=" ")
print()
