from pydantic import BaseModel


# pydantic may cast input data to force it to conform to model field types,
# and in some cases this may result in a loss of information
class Model(BaseModel):
    a: int
    b: float
    c: str


if __name__ == "__main__":
    print(Model(a=3.1415, b=" 2.72 ", c=123).dict())
