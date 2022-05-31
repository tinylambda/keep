class Structure:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) != len(self._fields):
            raise TypeError(f"expected {len(self._fields)} arguments")

        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        extra_args = kwargs.keys() - self._fields
        for name in extra_args:
            setattr(self, name, kwargs.pop(name))

        if kwargs:
            raise TypeError(f'duplicate values for {",".join(kwargs)}')


if __name__ == "__main__":

    class Stock(Structure):
        _fields = ["name", "shares", "price"]

    s1 = Stock("ACME", 50, 91.1)
    s2 = Stock("ACME", 50, 91.1, date="8/2/2012")
    s2 = Stock("ACME", 50, 91.1, date="8/2/2012", price=100)
