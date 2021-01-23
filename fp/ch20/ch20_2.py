class Quantity:
    __counter = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = "_{}#{}".format(prefix, index)
        print(self.storage_name, '!!!')
        cls.__counter += 1

    def __get__(self, instance, owner):
        return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.storage_name, value)
        else:
            raise ValueError('value must be > 0')


class LineItem:
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


if __name__ == '__main__':
    coconuts = LineItem('Braizilian coconut', 20, 17.95)

    print(
        coconuts.price,
        coconuts.weight
    )

    coconuts2 = LineItem('Braizilian coconut2', 21, 18.95)

    print(
        coconuts.price,
        coconuts.weight
    )
    print(
        coconuts2.price,
        coconuts2.weight
    )
    print(
        dir(coconuts)
    )

    print(
        getattr(coconuts, '_Quantity#0'),
        getattr(coconuts, '_Quantity#1')
    )

    print(dir(coconuts2))

    LineItem.weight
