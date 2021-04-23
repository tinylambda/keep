import sys


if __name__ == '__main__':

    s = '{name} has {n} messages'
    print(
        s.format(name='Guido', n=37)
    )

    name = 'Guido'
    n = 37
    print(
        s.format_map(vars())
    )


    class Info:
        def __init__(self, name, n):
            self.name = name
            self.n = n


    a = Info('Guido', 37)
    print(
        s.format_map(vars(a))
    )


    class SafeSub(dict):
        def __missing__(self, key):
            return '{' + key + '}'

    del n
    print(
        s.format_map(SafeSub(vars()))
    )


    def sub(text):
        return text.format_map(SafeSub(sys._getframe(1).f_locals))

    name = 'Guido'
    n = 37
    print(
        sub('Hello {name}')
    )
    print(
        sub('You have {n} messages.')
    )

    print(
        sub('Your favorite color is {color}')
    )

