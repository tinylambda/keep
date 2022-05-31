from typing import Optional

from pydantic import BaseModel, Field, ValidationError


class Model(BaseModel):
    a: Optional[int]

    # If you want to specify a field that can take a None value while still being required,
    # you can use Optional with ...:
    b: Optional[int] = ...
    c: Optional[int] = Field(...)


if __name__ == "__main__":
    print(Model(b=1, c=2))
    try:
        Model(a=1, b=2)
    except ValidationError as e:
        print(e)

    print(Model(a=1, b=2, c=None))
