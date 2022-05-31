import weakref


class Cached(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls.__cache = weakref.WeakValueDictionary()

    def __call__(cls, *args, **kwargs):
        if args in cls.__cache:
            return cls.__cache[args]
        else:
            obj = super().__call__(*args)
            cls.__cache[args] = obj
            return obj


class Spam(metaclass=Cached):
    def __init__(self, name):
        print("creating spam({!r})".format(name))
        self.name = name


if __name__ == "__main__":
    a = Spam("Guido")
    b = Spam("Felix")
    c = Spam("Guido")

    print(a is b)
    print(a is c)
