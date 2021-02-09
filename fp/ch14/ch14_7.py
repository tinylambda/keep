def gen_123():
    yield 1
    yield 2
    yield 3


if __name__ == '__main__':
    print(gen_123)
    print(gen_123())

    for i in gen_123():
        print(i)

    print('_' * 64)
    g = gen_123()
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))

