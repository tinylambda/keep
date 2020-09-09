print(
    max(1, 2, 3)
)

print(
    max((1, 2, 3, 4))
)


def g():
    for i in range(10):
        yield i


print(max(g()))

