import string


if __name__ == '__main__':
    name = 'Guido'
    n = 37
    print(
        '%(name)s has %(n)s messages.' % vars()
    )

    s = string.Template('$name has $n messages.')

    print(
        s.substitute(vars())
    )

