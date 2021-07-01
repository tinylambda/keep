if __name__ == '__main__':
    text = 'Hello World'

    print(
        text.ljust(20)
    )

    print(
        text.rjust(20)
    )

    print(
        text.center(20)
    )

    print(
        text.rjust(20, '=')
    )

    print(
        text.center(20, '*')
    )

    print('-' * 64)

    print(
        format(text, '>20')
    )

    print(
        format(text, '<20')
    )

    print(
        format(text, '^20')
    )

    print(
        format(text, '=>20s')
    )
    print(
        format(text, '*^20s')
    )

    print('-' * 64)

    print(
        '{:>10s} {:>10s}'.format('Hello', 'World')
    )

    print('-' * 64)

    x = 1.2345
    print(
        format(x, '>10')
    )

    print(
        format(x, '^10.2f')
    )

