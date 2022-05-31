import itertools

res = itertools.starmap(lambda x, y: x + y, zip([1, 2, 3], [4, 5, 6]))
print([item for item in res])

res2 = map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6])
print([item for item in res2])
