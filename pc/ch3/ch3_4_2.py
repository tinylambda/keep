if __name__ == '__main__':
    x = 1234
    print(
        bin(x)
    )

    print(
        oct(x)
    )

    print(
        hex(x)
    )

    print('-' * 64)

    print(format(x, 'b'))
    print(format(x, 'o'))
    print(format(x, 'x'))

    print('-' * 64)

    x = -1234
    print(format(x, 'b'))
    print(format(x, 'o'))
    print(format(x, 'x'))

    print('-' * 64)

    print(format(2 ** 32 + x, 'b'))
    print(format(2 ** 32 + x, 'x'))

    print('-' * 64)

    print(
        int('4d2', 16)
    )

    print(
        int('10011010010', 2)
    )


