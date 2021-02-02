import functools


def deco(f):
    @functools.wraps(f)
    def f(self):
        print(111)
    return f


class A:
    @deco
    def test(self):
        print('test')


if __name__ == '__main__':
    a = A()
    a.test()

    print(getattr(a, 'test'))

