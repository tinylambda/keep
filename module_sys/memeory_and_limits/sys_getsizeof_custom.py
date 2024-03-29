import sys


class WithAttributes:
    def __init__(self):
        self.a = "a"
        self.b = "b"
        return

    def __sizeof__(self):
        return object.__sizeof__(self) + sum(
            sys.getsizeof(v) for v in self.__dict__.values()
        )


if __name__ == "__main__":
    my_inst = WithAttributes()
    print(sys.getsizeof(my_inst))
