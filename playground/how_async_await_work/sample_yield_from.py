def lazy_range(up_to):
    index = 0

    def gratuitous_refactor():
        nonlocal index
        while index < up_to:
            yield index
            index += 1
    yield from gratuitous_refactor()


def genx():
    yield 42


def bottom():
    # return genx()  # won't work as expected
    return (yield 42)


def middle():
    return (yield from bottom())


def top():
    return (yield from middle())


if __name__ == '__main__':
    for i in lazy_range(3):
        print(i)

    print('-' * 64)

    gen = top()
    value = next(gen)
    print(value)

    try:
        value = gen.send(value * 10)
    except StopIteration as exc:
        print('got 1')
        value = exc.value
    print(value)

    try:
        value = gen.send(value * 10)
    except StopIteration as exc:
        print('got 2')
        value = exc.value
    print(value)
