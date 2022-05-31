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

print(len(flat))

a = zip(flat[0::2], flat[1::2])
print(list(a))

n = 3
b = zip(*(flat[i::n] for i in range(n)))
print(list(b))
