class Structure:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError(f"expected {len(self._fields)} arguments")

        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        for name in self._fields[len(args) :]:
            setattr(self, name, kwargs.pop(name))

        if kwargs:
            raise TypeError(f'invalid arguments: {",".join(kwargs)}')


if __name__ == "__main__":

    class Stock(Structure):
        _fields = ["name", "shares", "price"]

    s1 = Stock("ACME", 50, 91.1)
    s2 = Stock("ACME", 50, price=91.1)
    s3 = Stock("ACME", shares=50, price=91.1)
