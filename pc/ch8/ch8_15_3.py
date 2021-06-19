class A:
    def spam(self, x):
        print('A.spam', x)

    def foo(self):
        print('A.foo')


class B(A):
    def spam(self, x):
        print('B.spam')
        super().spam(x)

    def bar(self):
        print('B.bar')


if __name__ == '__main__':
    b = B()
    b.spam(87)
    b.foo()
    b.bar()
