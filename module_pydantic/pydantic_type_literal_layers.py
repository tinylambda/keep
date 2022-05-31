from typing import Literal, Optional, Union

from pydantic import BaseModel


class Dessert(BaseModel):
    kind: str


class Pie(Dessert):
    kind: Literal["pie"]
    flavor: Optional[str]


class ApplePie(Pie):
    flavor: Literal["apple"]


class PumpkinPie(Pie):
    flavor: Literal["pumpkin"]


class Meal(BaseModel):
    dessert: Union[ApplePie, PumpkinPie, Pie, Dessert]


if __name__ == "__main__":
    print(type(Meal(dessert={"kind": "pie", "flavor": "apple"}).dessert).__name__)
    print(type(Meal(dessert={"kind": "pie", "flavor": "pumpkin"}).dessert).__name__)
    print(type(Meal(dessert={"kind": "pie"}).dessert).__name__)
    print(type(Meal(dessert={"kind": "cake"}).dessert).__name__)
