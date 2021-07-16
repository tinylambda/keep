import inspect
import time
import types


class MultiMethod:
    """represents a single multimethod"""
    def __init__(self, name):
        self._methods = {}
        self.__name__ = name

    def register(self, meth):
        """register a new method as multimethod"""
        sig = inspect.signature(meth)
        # build a type signature from the method's annotations
        _types = []
        for name, param in sig.parameters.items():
            if name == 'self':
                continue
            if param.annotation is inspect.Parameter.empty:
                raise TypeError('Argument {} must be annotated with a type'.format(name))
            if not isinstance(param.annotation, type):
                raise TypeError('Argument {} annotation must be a type'.format(name))
            if param.default is not inspect.Parameter.empty:
                self._methods[tuple(_types)] = meth
            _types.append(param.annotation)

        self._methods[tuple(_types)] = meth

    def __call__(self, *args, **kwargs):
        """call a method based on type signature of the arguments"""
        _types = tuple(type(arg) for arg in args[1:])
        meth = self._methods.get(_types)
        if meth:
            return meth(*args)
        else:
            raise TypeError('No matching method for types {}'.format(_types))

    def __get__(self, instance, owner):
        """descriptor method needed to make calls work in a class"""
        if instance is not None:
            return types.MethodType(self, instance)
        else:
            return self


class MultiDict(dict):
    """special dictionary to build multimethod in a metaclass"""
    def __setitem__(self, key, value):
        if key in self:
            # if key already exists, it must be a multimethod or callable
            current_value = self[key]
            if isinstance(current_value, MultiMethod):
                current_value.register(value)
            else:
                mvalue = MultiMethod(key)
                mvalue.register(current_value)
                mvalue.register(value)
                super().__setitem__(key, mvalue)
        else:
            super().__setitem__(key, value)


class MultiMeta(type):
    """metaclass that allows multiple dispatch of methods"""
    def __new__(mcs, clsname, bases, clsdict):
        return type.__new__(mcs, clsname, bases, dict(clsdict))

    @classmethod
    def __prepare__(metacls, name, bases):
        return MultiDict()


class Spam(metaclass=MultiMeta):
    def bar(self, x: int, y: int):
        print('Bar 1:', x, y, [type(x), type(y)])

    def bar(self, _s: str, n: int = 0):
        print('Bar 2:', _s, n, [type(_s), type(n)])


class Date(metaclass=MultiMeta):
    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day

    def __init__(self):
        t = time.localtime()
        self.__init__(t.tm_year, t.tm_mon, t.tm_mday)


if __name__ == '__main__':
    s = Spam()
    s.bar(2, 3)
    s.bar('hello', 2)
    s.bar('hello')
    try:
        s.bar(2, 'hello')
    except TypeError as e:
        print(e)

    d = Date(2012, 12, 21)
    e = Date()
    print(e.year, e.month, e.day)

