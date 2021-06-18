class A:
    def spam(self, x):
        pass

    def foo(self):
        pass


class B:
    def __init__(self):
        self._a = A()

    def bar(self):
        pass

    def __getattr__(self, item):
        return getattr(self._a, item)


if __name__ == '__main__':
    b = B()
    b.foo()
    b.bar()
    b.spam(100)

