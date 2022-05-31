from collections import abc


class Foo:
    def __iter__(self):
        pass


if __name__ == "__main__":
    print(issubclass(Foo, abc.Iterable))

    f = Foo()
    print(isinstance(f, abc.Iterable))
