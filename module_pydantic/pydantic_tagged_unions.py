from typing import Literal, Union

from pydantic import BaseModel, Field, ValidationError


class Cat(BaseModel):
    pet_type: Literal["cat"]
    meows: int


class Dog(BaseModel):
    pet_type: Literal["dog"]
    barks: int


class Lizard(BaseModel):
    pet_type: Literal["reptile", "lizard"]
    scales: bool


class Model(BaseModel):
    pet: Union[Cat, Dog, Lizard] = Field(..., discriminator="pet_type")
    n: int


if __name__ == "__main__":
    print(Model(pet={"pet_type": "dog", "barks": 3.14}, n=1))
    try:
        Model(pet={"pet_type": "dog"}, n=1)
    except ValidationError as e:
        print(e)
