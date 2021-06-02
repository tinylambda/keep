class A:
    def spam(self):
        print('A.spam')
        super().spam()


class B:
    def spam(self):
        print('B.spam')


class C(A, B):
    pass


if __name__ == '__main__':
    a = A()
    try:
        a.spam()
    except AttributeError as e:
        print(e)

    c = C()
    c.spam()

    print(C.__mro__)

