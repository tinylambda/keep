import keyword
from collections import abc
from ch19_1 import load


class FrozenJSON:
    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            r = super().__new__(cls)
            print(r, type(r))
            return r
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg

    def __init__(self, mapping):
        self.__data = mapping
        for k, v in mapping.items():
            if keyword.iskeyword(k):
                k += '_'
            self.__data[k] = v

    def __getattr__(self, item):
        if hasattr(self.__data, item):
            return getattr(self.__data, item)
        else:
            return FrozenJSON(self.__data)


if __name__ == '__main__':
    feed = load()
    FrozenJSON(feed)
