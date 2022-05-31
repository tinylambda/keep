import dataclasses
from dataclasses import dataclass


@dataclass
class Picture:
    url: str
    img_type: str


@dataclass
class InventoryItem:
    name: str
    unit_price: float
    picture_info: Picture
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand


if __name__ == "__main__":
    picture_info = Picture("http://www.example.com/a.png", "png")
    inventory_item = InventoryItem("test", 3.4, picture_info, 10)
    print(dataclasses.asdict(inventory_item))
