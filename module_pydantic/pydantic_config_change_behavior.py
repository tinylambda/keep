from pydantic import BaseModel as PydanticBaseModel


class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True


class MyClass:
    pass


class Model(BaseModel):
    x: MyClass

