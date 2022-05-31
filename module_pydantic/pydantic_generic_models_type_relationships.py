from typing import TypeVar, Generic

from pydantic import ValidationError
from pydantic.generics import GenericModel

T = TypeVar("T")


class InnerT(GenericModel, Generic[T]):
    inner: T


class OuterT(GenericModel, Generic[T]):
    outer: T
    nested: InnerT[T]


nested = InnerT[int](inner=1)
print(OuterT[int](outer=1, nested=nested))

try:
    nested = InnerT[str](inner="ac")
    print(OuterT[int](outer="go", nested=nested))
except ValidationError as e:
    print(e)
