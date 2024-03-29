class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Typed(Descriptor):
    expected_type = type(None)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError("expected " + str(self.expected_type))
        super().__set__(instance, value)


class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("expected >= 0")
        super().__set__(instance, value)


class MaxSized(Descriptor):
    def __init__(self, name=None, **opts):
        if "size" not in opts:
            raise TypeError("missing size option")
        super().__init__(name, **opts)

    def __set__(self, instance, value):
        if len(value) > self.size:
            raise ValueError(f"size must be < {self.size}")
        super().__set__(instance, value)


class Integer(Typed):
    expected_type = int


class UnsignedInteger(Integer, Unsigned):
    pass


class Float(Typed):
    expected_type = float


class UnsignedFloat(Float, Unsigned):
    pass


class String(Typed):
    expected_type = str


class SizedString(String, MaxSized):
    pass


class Stock:
    name = SizedString("name", size=8)
    shares = UnsignedInteger("shares")
    price = UnsignedFloat("price")

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


if __name__ == "__main__":
    s = Stock("ACME", 50, 91.1)
    print(s.name)
    print(s.shares)
    print(s.price)
    s.shares = 75
    try:
        s.shares = -10
    except ValueError as e:
        print(e)

    try:
        s.price = "a lot"
    except TypeError as e:
        print(e)

    try:
        s.name = "AAAAABBBBCCCCDD"
    except ValueError as e:
        print(e)
