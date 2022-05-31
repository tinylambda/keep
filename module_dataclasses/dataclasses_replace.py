import typing
from dataclasses import dataclass
from dataclasses import replace


@dataclass
class C:
    x: int
    y: typing.Any
    z: int = 5

    def add_one(self):
        return self.x + 1


if __name__ == "__main__":
    c = C(x=100, y="hello")
    print(c)
    c_copy = replace(c, x=1000)
    print(c_copy)
    print(c.add_one())
    print(c_copy.add_one())
