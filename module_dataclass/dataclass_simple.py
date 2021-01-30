from dataclasses import dataclass


@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand


if __name__ == '__main__':
    i = InventoryItem('Test Item', 9.7, 88)
    print(i.total_cost())

