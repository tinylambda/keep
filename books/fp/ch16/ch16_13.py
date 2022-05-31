def gen():
    for c in "AB":
        yield c
    for i in range(1, 3):
        yield i


def gen2():
    yield from "AB"
    yield from range(1, 3)


def chain(*iterables):
    for it in iterables:
        yield from it


if __name__ == "__main__":
    print(list(gen()))

    print(list(gen2()))

    print(list(chain("AB", range(1, 3))))
