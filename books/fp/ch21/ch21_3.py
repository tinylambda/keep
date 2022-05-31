import abc
import collections


if __name__ == "__main__":
    print("spam".__class__)
    print(str.__class__)
    print(type.__class__)

    assert issubclass(type, object)
    assert isinstance(object, type)

    print(collections.Iterable.__class__)
    print(abc.ABCMeta.__class__)
    print(abc.ABCMeta.__mro__)
