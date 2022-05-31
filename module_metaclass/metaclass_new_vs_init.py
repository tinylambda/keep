class MetaOne(type):
    def __new__(mcs, name, bases, cls_dict):
        """
        __new__ is used when one wants to define dict or bases tuples before
        the class is created. The return value of __new__ is usually an instance
        of cls.
        __new__ allows subclasses of immutable types to customize instance creation.
        It can be overridden in custom metaclass to custom metaclass to customize
        class creation.
        """
        cls = type.__new__(mcs, name, bases, cls_dict)
        i = cls()
        print("cls is ", i)
        return i

    def __init__(cls, what, bases=None, d=None):
        print("init...")
        print(what, bases, d)

    def __call__(cls, *args, **kwargs):
        print("in __call__", args, kwargs)
        return cls


class MetaTwo(type):
    def __init__(cls, name, bases, cls_dict):
        """
        __init__ is usually after the object has been created so as to initialize it.
        """
        obj = super(MetaTwo, cls).__init__(name, bases, cls_dict)
        print("obj is ", obj)
        return obj


class A(metaclass=MetaOne):
    pass


A()
