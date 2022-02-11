from pydantic import BaseModel, ValidationError, Field


class Model(BaseModel):
    a: int
    b: int = ...  # will not work well with mypy
    c: int = Field(...)


if __name__ == '__main__':
    try:
        Model()
    except ValidationError as e:
        print(e)
