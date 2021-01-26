class A:
    x = 1000

    def __init__(self):
        pass

    def test(self):
        return self.x


if __name__ == '__main__':
    a = A()
    print(a.test())

    a.x = 2000
    print(a.x, A.x)

