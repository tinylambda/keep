
if __name__ == '__main__':
    x = 1234.5678
    print(
        format(x, '0.2f')
    )

    print(
        format(x, '>10.1f')
    )

    print(
        format(x, '<10.1f')
    )

    print(
        format(x, '^10.1f')
    )

    print(
        format(x, ',')
    )

    print(
        format(x, '0,.1f')
    )

    print(
        format(x, 'e')
    )

    print(
        format(x, '0.2E')
    )

    print('the value is {:0,.2f}'.format(x))

