flat = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
]
flat_iter = iter(flat)

N = 3
g = (tuple(next(flat_iter) for i in range(N)) for row in range(len(flat) // N))
print(list(g))

remain_items = []
for remain_item in flat_iter:
    remain_items.append(remain_item)

remain_items_len = len(remain_items)
how_many_to_add = N - remain_items_len

if how_many_to_add < N:
    for _ in range(how_many_to_add):
        remain_items.append(None)

    print(tuple(remain_items))
