import timeit


class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value


if __name__ == '__main__':
    a = A(1, 2)
    x = timeit.timeit('a.x', 'from __main__ import a')
    print(x)

    y = timeit.timeit('a.y', 'from __main__ import a')
    print(y)
