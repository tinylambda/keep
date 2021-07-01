headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]

print(
    dict(zip(headers, values))
)

print('-' * 64)

for name, val in zip(headers, values):
    print(name, '=', val)

print('-' * 64)

a = [1, 2, 3]
b = [10, 11, 12]
c = ['x', 'y', 'z']

for i in zip(a, b, c):
    print(i)

print('-' * 64)

print(
    zip(a, b)
)

print(
    list(zip(a, b))
)

