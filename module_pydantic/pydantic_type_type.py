from typing import Type

from pydantic import BaseModel, ValidationError


class Foo:
    pass


class Bar(Foo):
    pass


class Other:
    pass


# pydantic supports the use of Type[T]
# to specify that a field may only accept classes (not instances) that are subclasses of T.
class SimpleModel(BaseModel):
    just_subclasses: Type[Foo]


class LenientSimpleModel(BaseModel):
    any_class_goes: Type


if __name__ == '__main__':
    print(SimpleModel(just_subclasses=Foo))
    print(SimpleModel(just_subclasses=Bar))

    try:
        SimpleModel(just_subclasses=Other)
    except ValidationError as e:
        print(e)

    print(LenientSimpleModel(any_class_goes=int))
    print(LenientSimpleModel(any_class_goes=Foo))

    try:
        LenientSimpleModel(any_class_goes=Foo())
    except ValidationError as e:
        print(e)
