import json
from typing import List, Dict

from pydantic import BaseModel, ValidationError
from pydantic.schema import schema


class Pets(BaseModel):
    __root__: List[str]


if __name__ == "__main__":
    print(Pets(__root__=["dog", "cat"]))
    print(Pets(__root__=["dog", "cat"]).json())
    print(Pets.schema())

    pets_schema = schema([Pets])
    print(json.dumps(pets_schema, indent=2))

    print(Pets.parse_obj(["dog", "cat"]))
    print(Pets.parse_obj({"__root__": ["dog", "cat"]}))

    class PetsByName(BaseModel):
        __root__: Dict[str, str]

    print(PetsByName.parse_obj({"Otis": "dog", "Milo": "cat"}))
    try:
        # If the custom root type is a mapping type (eg., Dict or Mapping),
        # the argument itself is always validated against the custom root type.
        PetsByName.parse_obj({"__root__": {"Otis": "dog", "Milo": "cat"}})
    except ValidationError as e:
        print(e)
