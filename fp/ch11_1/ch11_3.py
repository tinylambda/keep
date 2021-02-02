from collections import abc
from collections import MutableSequence
from random import shuffle


class Struggle:
    def __len__(self):
        return 23


class Struggle2:
    def insert(self, index, value):
        self.__data[index] = value

    def __init__(self):
        self.__data = [1, 2, 3]

    def __len__(self):
        return len(self.__data)

    def __iter__(self):
        return iter(self.__data)

    def __getitem__(self, item):
        return self.__data[item]

    def __setitem__(self, key, value):
        self.__data[key] = value

    def __delitem__(self, key):
        del self.__data[key]

    def __contains__(self, item):
        return item in self.__data

    def __reversed__(self):
        return reversed(self.__data)


if __name__ == '__main__':
    l = list(range(10))
    shuffle(l)
    print(l)

    print(isinstance(Struggle(), abc.Sized))

    s2 = Struggle2()
    print(s2[1])
    print(isinstance(s2, abc.Sequence))

