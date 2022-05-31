from collections import namedtuple
from typing import NamedTuple

from pydantic import (
    create_model,
    BaseModel,
    validator,
    ValidationError,
    create_model_from_typeddict,
    create_model_from_namedtuple,
)
from typing_extensions import TypedDict

DynamicFoobarModel = create_model("DynamicFoobarModel", foo=(str, ...), bar=123)


class StaticFoobarModel(BaseModel):
    foo: str
    bar = 123


# Here StaticFoobarModel and DynamicFoobarModel are identical.


class FooModel(BaseModel):
    foo: str
    bar = 123


# Use __base__ to specify base class
BarModel = create_model("BarModel", apple="russet", banana="yellow", __base__=FooModel)
print(BarModel)
print(BarModel.__fields__.keys())


# use __validators__ to specify validators


def username_alphanumeric(cls, v: str):
    assert v.isalnum()
    return v


validators = {"username_validator": validator("username")(username_alphanumeric)}

UserModel = create_model("UserModel", username=(str, ...), __validators__=validators)

user = UserModel(username="felix")
print(user)

try:
    UserModel(username="felix@github")
except ValidationError as e:
    print(e)


# create_model_from_typeddict


class User(TypedDict):
    name: str
    id: int


class Config:
    extra = "forbid"


UserM = create_model_from_typeddict(User, __config__=Config)
print(repr(UserM(name=123, id="3")))

try:
    UserM(name=123, id="3", other="no")
except ValidationError as e:
    print(e)

UserTuple = namedtuple("UserTuple", ["name", "id"])
UserM2 = create_model_from_namedtuple(UserTuple)
print(repr(UserM2(name=123, id="3")))


class AnotherUserTuple(NamedTuple):
    name: str
    id: int


UserM3 = create_model_from_namedtuple(AnotherUserTuple)
print(repr(UserM3(name=123, id="3")))

print(AnotherUserTuple("Felix", 1234)._asdict())
print(UserM3.parse_obj(AnotherUserTuple("Felix", 1234)._asdict()))
