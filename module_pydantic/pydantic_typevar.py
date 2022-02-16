from typing import TypeVar

from pydantic import BaseModel

Foobar = TypeVar('Foobar')
BoundFloat = TypeVar('BoundFloat')
IntOrStr = TypeVar('IntOrStr', int, str)


class Model(BaseModel):
    a: Foobar
    b: BoundFloat
    c: IntOrStr


if __name__ == '__main__':
    print(Model(a=[1], b=4.2, c=1))
    print(Model(b=4.1, c='w'))
