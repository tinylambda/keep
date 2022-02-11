from typing import List

from pydantic import BaseModel, parse_obj_as


class Item(BaseModel):
    id: int
    name: str


if __name__ == '__main__':
    item_data = [{'id': 1, 'name': 'My Item'}]
    items = parse_obj_as(List[Item], item_data)
    print(items)

    # Pydantic also includes two similar standalone
    # functions called parse_file_as and parse_raw_as, which are analogous
    # to BaseModel.parse_file and BaseModel.parse_raw.
