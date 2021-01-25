import weakref


if __name__ == '__main__':
    s1 = {1, 2, 3}
    s2 = s1

    def bye():
        print('Gone with the wind...')

    ender = weakref.finalize(s1, bye)
    print(
        ender.alive
    )
    del s1
    print(ender.alive)

    s2 = 'spam'
    print(ender.alive)

