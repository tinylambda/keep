import dataclasses
from dataclasses import dataclass


@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand


if __name__ == '__main__':
    item = InventoryItem('item1', 5.6, 10)
    print(dataclasses.asdict(item))  # can transform to json using json.dumps

    item = InventoryItem(name='item2', unit_price=5.7, quantity_on_hand=10)  # keyword args also works
    print(dataclasses.asdict(item))

