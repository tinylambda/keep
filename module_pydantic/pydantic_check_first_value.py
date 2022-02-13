import itertools
from typing import Iterable

from pydantic import BaseModel, validator, ValidationError
from pydantic.fields import ModelField


class Model(BaseModel):
    infinite: Iterable[int]

    @validator('infinite')
    def infinite_first_int(cls, iterable, field: ModelField):
        first_value = next(iterable)

        if field.sub_fields:
            sub_field = field.sub_fields[0]
            v, error = sub_field.validate(first_value, {}, loc='first_value')
            if error:
                raise ValidationError([error], cls)
        return itertools.chain([first_value], iterable)


def infinite_ints():
    i = 0
    while True:
        yield i
        i += 1


def infinite_strs():
    while True:
        for letter in 'allthesingleladies':
            yield letter


if __name__ == '__main__':
    m = Model(infinite=infinite_ints())
    print(m)

    try:
        Model(infinite=infinite_strs())
    except ValidationError as e:
        print(e)
