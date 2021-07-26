def gen():
    print('start gen')
    for i in range(3):
        yield i
    print('end gen')
    return i


if __name__ == '__main__':
    g = gen()
    next(g)
    next(g)
    next(g)
    next(g)  # will trigger StopIteration with value 2



