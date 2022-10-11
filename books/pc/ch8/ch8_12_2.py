import io
from abc import ABCMeta, abstractmethod


class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


class SocketStream(IStream):
    def read(self, maxbytes=-1):
        pass

    def write(self, data):
        pass


class A(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @classmethod
    @abstractmethod
    def method1(cls):
        pass

    @staticmethod
    @abstractmethod
    def method2():
        pass


if __name__ == "__main__":
    # a = IStream()  # Can't instantiate abstract class IStream with abstract methods read, write

    s = SocketStream()

    IStream.register(io.IOBase)
    f = open("/tmp/test.txt", "w")
    print(isinstance(f, IStream))
