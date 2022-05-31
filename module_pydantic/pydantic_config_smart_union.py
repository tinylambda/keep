from typing import Union, List

from pydantic import BaseModel


class Foo(BaseModel):
    pass


class Bar(BaseModel):
    pass


class Model(BaseModel):
    x: Union[str, int]
    y: Union[Foo, Bar]


class Model2(BaseModel):
    x: Union[str, int]
    y: Union[Foo, Bar]

    class Config:
        smart_union = True


# Note that smart_union option does not support compound types yet
class Model3(BaseModel, smart_union=True):
    x: Union[List[str], List[int]]


if __name__ == "__main__":
    print(Model(x=1, y=Bar()))
    print(Model2(x=1, y=Bar()))
    print(Model3(x=[1, "2"]))
    print(Model3(x=[1, 2]))
