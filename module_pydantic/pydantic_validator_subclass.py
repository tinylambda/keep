from typing import List

from pydantic import BaseModel, validator, ValidationError


class ParentModel(BaseModel):
    names: List[str]


class ChildModel(ParentModel):
    @validator('names', each_item=True)
    def check_names_not_empty(cls, v):
        assert v != '', 'Empty strings are not allowed'
        return v


class ChildModel2(ParentModel):
    @validator('names')
    def check_names_not_empty(cls, v):
        for name in v:
            assert name != '', 'Empty strings are not allowed'
        return v


if __name__ == '__main__':
    # If using a validator with a subclass that references a List type field on a parent class, using each_item=True
    # will cause the validator not to run; instead, the list must be iterated over programmatically.
    try:
        child = ChildModel(names=['Alice', 'Felix', 'Eve', ''])
    except ValidationError as e:
        print(e)
    else:
        print('No validation error caught.')

    try:
        child = ChildModel2(names=['Alice', 'Felix', 'Eve', ''])
    except ValidationError as e:
        print(e)
