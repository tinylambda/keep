from collections import OrderedDict


class NoDupOrderedDict(OrderedDict):
    def __init__(self, clsname):
        self.clsname = clsname
        super().__init__()

    def __setitem__(self, key, value):
        if key in self:
            raise TypeError(f'{key} already defined in {self.clsname}')
        super().__setitem__(key, value)


class OrderedMeta(type):
    def __new__(mcs, clsname, bases, clsdict):
        d = dict(clsdict)
        d['_order'] = [name for name in clsdict if name[0] != '_']
        return type.__new__(mcs, clsname, bases, d)

    @classmethod
    def __prepare__(metacls, name, bases):
        return NoDupOrderedDict(name)


class A(metaclass=OrderedMeta):
    def spam(self):
        pass

    def spam(self):
        pass

