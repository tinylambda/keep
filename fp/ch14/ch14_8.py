def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end')


if __name__ == '__main__':
    for c in gen_AB():
        print('-->', c)

