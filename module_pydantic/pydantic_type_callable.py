from typing import Callable

from pydantic import BaseModel


class Foo(BaseModel):
    callback: Callable[[int], int]


# Callable fields only perform a simple check that the argument is callable;
# no validation of arguments, their types, or the return type is performed.
class Bar(BaseModel):
    callback: Callable[[int, int], int]


if __name__ == "__main__":
    m = Foo(callback=lambda x: 2 * x)
    print(m)
    print(m.callback(100))

    m = Bar(callback=lambda x, y: x + y)
    print(m)
    print(m.callback(10, 20))
