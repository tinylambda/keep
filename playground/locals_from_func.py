class A:
    def myfunc():
        doc = "this is the doc"

        def fget(self):
            return "abc"

        return locals()

    m = property(**myfunc())

    @property
    def n(self):
        return "def"


if __name__ == "__main__":
    a = A()
    print(a.m)
    print(a.n)
