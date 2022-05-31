from dataclasses import dataclass


@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand


if __name__ == "__main__":
    item = InventoryItem("item1", 5.6, 10)
    print(item.total_cost())

    print(item)
