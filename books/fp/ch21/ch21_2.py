class Validated:
    def __init__(self):
        self.name = None

    def __get__(self, instance, owner):
        print("in get")

    def __set__(self, instance, value):
        print("in set")
        setattr(instance, self.name, value)


def entity(cls):
    for key, attr in cls.__dict__.items():
        print("Checking: ", key)
        if isinstance(attr, Validated):
            type_name = type(attr).__name__
            attr.name = "_{}#{}".format(type_name, key)
    return cls


@entity
class LineItem:
    description = Validated()
    weight = Validated()
    price = Validated()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


if __name__ == "__main__":
    raisins = LineItem("Golden raisins", 10, 6.95)

    print(dir(raisins))

    print()
