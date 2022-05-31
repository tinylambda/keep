from typing import TypeVar, Generic

from pydantic import ValidationError
from pydantic.generics import GenericModel

AT = TypeVar("AT")
BT = TypeVar("BT")


class Model(GenericModel, Generic[AT, BT]):
    a: AT
    b: BT


# If you don't specify parameters before instantiating the generic model, they will be treated as Any
print(Model(a="a", b="b"))

IntT = TypeVar("IntT", bound=int)
typevar_model = Model[int, IntT]
print(typevar_model(a=1, b=1))

try:
    typevar_model(a="a", b="a")
except ValidationError as e:
    print(e)


concret_model = typevar_model[int]
print(typevar_model(a=1, b=1))
