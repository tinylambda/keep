import abc
import types


def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price


def cost(self):
    return self.shares * self.price


cls_dict = {
    "__init__": __init__,
    "cost": cost,
}


Stock = types.new_class(
    "Stock", (), {"metaclass": abc.ABCMeta}, lambda ns: ns.update(cls_dict)
)
Stock.__module__ = __name__


if __name__ == "__main__":
    print(Stock)
    print(type(Stock))
