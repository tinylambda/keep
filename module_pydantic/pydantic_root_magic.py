from typing import List

from pydantic import BaseModel


class Pets(BaseModel):
    __root__: List[str]

    def __iter__(self):
        return iter(self.__root__)

    def __getitem__(self, item):
        return self.__root__[item]


if __name__ == "__main__":
    pets = Pets.parse_obj(["dog", "cat"])
    print(pets[0])
    print([pet for pet in pets])
