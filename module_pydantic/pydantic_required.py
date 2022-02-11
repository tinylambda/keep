from pydantic import BaseModel, ValidationError, Field


class Model(BaseModel):
    a: int
    b: int = ...
    c: int = Field(...)


if __name__ == '__main__':
    try:
        Model()
    except ValidationError as e:
        print(e)
