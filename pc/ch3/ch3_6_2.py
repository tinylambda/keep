import cmath


if __name__ == '__main__':
    a = complex(2, 4)
    b = 3 - 5j
    print(a)
    print(b)

    print(a.real)
    print(a.imag)

    print(
        a.conjugate()
    )

    print(
        a + b
    )

    print(
        a * b
    )

    print(
        a / b
    )

    print(
        abs(a)
    )

    print('-' * 64)

    print(
        cmath.sin(a)
    )

    print(
        cmath.cos(a)
    )

    print(
        cmath.exp(a)
    )

