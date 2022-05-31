def reader():
    for i in range(4):
        yield f"<< {i}"


def reader_wrapper(g):
    for v in g:
        yield v


def reader_wrapper2(g):
    yield from g


if __name__ == "__main__":
    wrap = reader_wrapper(reader())
    for i in wrap:
        print(i)

    print("-" * 64)

    wrap2 = reader_wrapper2(reader())
    for i in wrap2:
        print(i)
