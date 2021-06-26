class A:
    @classmethod
    def method(cls):
        print('go')


class B:
    def method(self):
        print('go')
    method = classmethod(method)


class C:
    def method(self):
        print('go')


if __name__ == '__main__':
    A.method()
    B.method()
    C.method()  # this will raise TypeError

