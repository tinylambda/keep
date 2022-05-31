def lazy_range(up_to):
    index = 0

    def gratuitous_refactor():
        nonlocal index
        while index < up_to:
            yield index
            index += 1

    yield from gratuitous_refactor()


if __name__ == "__main__":
    for i in lazy_range(10):
        print(i)
