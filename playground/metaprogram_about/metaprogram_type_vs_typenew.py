class MetaA(type):
    def __new__(mcs, clsname, bases, class_dict: dict):
        # calling parent's new
        cls = type.__new__(mcs, clsname, bases, class_dict)
        return cls

    def __init__(cls, name, bases, class_dict):
        # this will be executed
        print("MetaA.__init__")
        super(MetaA, cls).__init__(name, bases, class_dict)


class MetaB(type):
    def __new__(mcs, clsname, bases, class_dict: dict):
        # creating a whole new class
        cls = type(clsname, bases, class_dict)
        return cls

    def __init__(cls, name, bases, class_dict):
        # this will not be executed
        print("MetaB.__init__")
        super(MetaB, cls).__init__(name, bases, class_dict)


class A(metaclass=MetaA):
    pass


class B(metaclass=MetaB):
    pass
