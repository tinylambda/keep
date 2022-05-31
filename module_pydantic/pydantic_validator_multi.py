from typing import List

from pydantic import BaseModel, validator, ValidationError


class DemoModel(BaseModel):
    square_numbers: List[int] = []
    cube_numbers: List[int] = []

    @validator("*", pre=True)
    def split_str(cls, v):
        if isinstance(v, str):
            return v.split("|")
        return v

    @validator("cube_numbers", "square_numbers")
    def check_sum(cls, v):
        if sum(v) > 42:
            raise ValueError("sum of numbers greater than 42")
        return v

    @validator("square_numbers", each_item=True)
    def check_squares(cls, v):
        assert v**0.5 % 1 == 0, f"{v} is not a square number"
        return v

    @validator("cube_numbers", each_item=True)
    def check_cubes(cls, v):
        assert v ** (1 / 3) % 1 == 0, f"{v} is not a cubed number"
        return v


if __name__ == "__main__":
    print(DemoModel(square_numbers=[1, 4, 9]))
    print(DemoModel(square_numbers="1|4|9"))
    print(DemoModel(square_numbers=[16], cube_numbers=[8, 27]))

    try:
        DemoModel(square_numbers=[1, 4, 12])
    except ValidationError as e:
        print(e)

    try:
        DemoModel(cube_numbers=[27, 27])
    except ValidationError as e:
        print(e)
