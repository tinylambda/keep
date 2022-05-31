import types


class multimethod:
    def __init__(self, func):
        self._methods = {}
        self.__name__ = func.__name__
        self._default = func

    def match(self, *_types):
        def register(func):
            ndefaults = len(func.__defaults__) if func.__defaults__ else 0
            for n in range(ndefaults + 1):
                self._methods[_types[: len(_types) - n]] = func
            return self

        return register

    def __call__(self, *args):
        _types = tuple(type(arg) for arg in args[1:])
        meth = self._methods.get(_types)
        if meth:
            return meth(*args)
        else:
            return self._default(*args)

    def __get__(self, instance, owner):
        if instance is not None:
            return types.MethodType(self, instance)
        else:
            return self


if __name__ == "__main__":

    class Spam:
        @multimethod
        def bar(self, *args):
            raise TypeError("no matching method for bar")

        @bar.match(int, int)
        def bar(self, x, y):
            print("bar 1:", x, y)

        @bar.match(str, int)
        def bar(self, _s, n=0):
            print("bar 2:", _s, n)

    s = Spam()
    s.bar(1, 2)
    s.bar("hello", 100)
    try:
        s.bar(100, "hello")
    except Exception as e:
        print(e)
