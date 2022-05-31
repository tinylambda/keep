class ServerMeta(type):
    def __new__(mcs, clsname, bases, clsdict):
        cls = type.__new__(mcs, clsname, bases, clsdict)
        print(clsdict)
        return cls


class Server(metaclass=ServerMeta):
    NAME = "BASE"
    pass
