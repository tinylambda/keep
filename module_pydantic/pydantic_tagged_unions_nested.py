from typing import Literal, Annotated, Union

from pydantic import BaseModel, Field, ValidationError


class BlackCat(BaseModel):
    pet_type: Literal['cat']
    color: Literal['black']
    black_name: str


class WhiteCat(BaseModel):
    pet_type: Literal['cat']
    color: Literal['white']
    white_name: str


Cat = Annotated[Union[BlackCat, WhiteCat], Field(discriminator='color')]
# same as
# class Cat(BaseModel):
#     __root__: Annotated[Union[BlackCat, WhiteCat], Field(discriminator='color')]


class Dog(BaseModel):
    pet_type: Literal['dog']
    name: str


Pet = Annotated[Union[Cat, Dog], Field(discriminator='pet_type')]


class Model(BaseModel):
    pet: Pet
    n: int


if __name__ == '__main__':
    m = Model(pet={'pet_type': 'cat', 'color': 'black', 'black_name': 'felix'}, n=1)
    print(m)

    try:
        m = Model(pet={'pet_type': 'cat', 'color': 'red', 'black_name': 'felix'}, n='1')
    except ValidationError as e:
        print(e)

    try:
        Model(pet={'pet_type': 'cat', 'color': 'black'}, n=1)
    except ValidationError as e:
        print(e)
