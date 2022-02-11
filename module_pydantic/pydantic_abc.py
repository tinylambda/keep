import abc

from pydantic import BaseModel


class FooBarModel(BaseModel, abc.ABC):
    a: str
    b: int

    @abc.abstractmethod
    def my_abstract_method(self):
        pass


try:
    # abstract class with abstract method cannot be initialized
    foobar = FooBarModel(a='hello', b=100)
except TypeError as e:
    print(e)
