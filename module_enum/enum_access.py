from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


if __name__ == "__main__":
    print(Color(1))
    print(Color["RED"])

    member = Color.RED
    print(member.name)
    print(member.value)
