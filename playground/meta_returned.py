class Meta(type):
    def __new__(mcs, name, bases, class_dict):
        r = type.__new__(mcs, name, bases, class_dict)
        print(r, type(r))
        print(isinstance(r, mcs))
        return r


class MyClass(metaclass=Meta):
    pass


mc = MyClass()
print(mc, type(mc))

