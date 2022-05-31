from typing import TypedDict


# `total=False` means keys are non-required
from pydantic import BaseModel, Extra, ValidationError


class UserIdentity(TypedDict, total=False):
    name: str
    surname: str


class User(TypedDict):
    identity: UserIdentity
    age: int


class Model(BaseModel):
    u: User

    class Config:
        extra = Extra.forbid


if __name__ == "__main__":
    print(Model(u={"identity": {"name": "Pan", "surname": "Felix"}, "age": 35}))

    print(Model(u={"identity": {"name": None, "surname": "Felix"}, "age": 35}))

    print(Model(u={"identity": {}, "age": 35}))

    try:
        Model(u={"identity": {"name": ["Pan"], "surname": "Felix"}, "age": 21})
    except ValidationError as e:
        print(e)
