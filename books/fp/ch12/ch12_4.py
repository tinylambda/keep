class A:
    def ping(self):
        print('ping:', self)


class B(A):
    def pong(self):
        print('pong:', self)


class C(A):
    def pong(self):
        print('PONG:', self)


class D(B, C):
    def ping(self):
        super().ping()
        print('post-ping:', self)

    def pingpong(self):
        self.ping()
        super().ping()

        self.pong()
        super().pong()
        C.pong(self)


if __name__ == '__main__':
    d = D()
    d.pong()
    C.pong(d)

    print(D.__mro__)
    print(D.mro())

    d.ping()

    print('d.pingpong(): ')
    d.pingpong()

