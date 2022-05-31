class NoMixedCaseMeta(type):
    def __new__(mcs, clsname, bases, clsdict):
        for name in clsdict:
            if name.lower() != name:
                raise TypeError(f"bad attribute name: {name}")
        return super().__new__(mcs, clsname, bases, clsdict)


class Root(metaclass=NoMixedCaseMeta):
    pass


class A(Root):
    def foo_bar(self):
        pass


class B(Root):
    def fooBar(self):
        pass
