x = [1, 2, 3]


def g():
    yield from x


if __name__ == "__main__":
    for item in g():
        print(item)
