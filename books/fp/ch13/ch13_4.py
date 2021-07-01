class A:
    def __init__(self, x):
        self._x = x

    def __add__(self, other):
        if isinstance(other, A):
            return A(self._x + other._x)
        else:
            return NotImplemented

    def __iadd__(self, other):
        self._x += other._x
        return self

    def __repr__(self):
        return f'A({self._x})'


if __name__ == '__main__':
    a1 = A(1)
    a2 = A(2)

    print(a1)

    print(id(a1))
    a1 += a2
    print(id(a1))

    print(a1)

    print('_' * 100)
    a1 = A(1)
    a2 = A(2)
    print(id(a1))
    a1 = a1 + a2
    print(a1, id(a1))

