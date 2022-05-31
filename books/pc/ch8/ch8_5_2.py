class A:
    def __init__(self):
        self._internal = 0
        self.public = 1

    def public_method(self):
        pass

    def _internal_method(self):
        pass


class B:
    def __init__(self):
        self.__private = 0

    def __private_method(self):
        print("__private_method in B")

    def public_method(self):
        pass


class C(B):
    def __init__(self):
        super(C, self).__init__()
        self.__private = 1

    def __private_method(self):
        print("__private_method in C")


if __name__ == "__main__":
    c = C()
    print(dir(c))

    print(c._C__private)
    print(c._B__private)  # keep original value 0
