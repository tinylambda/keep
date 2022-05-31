from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement


items = ["a", "b", "c"]
for p in permutations(items):
    print(p)

print("-" * 64)

for p in permutations(items, 2):
    print(p)

print("-" * 64)

for c in combinations(items, 3):
    print(c)

print("-" * 64)

for c in combinations(items, 2):
    print(c)

print("-" * 64)

for c in combinations(items, 1):
    print(c)

print("-" * 64)

for c in combinations_with_replacement(items, 3):
    print(c)
