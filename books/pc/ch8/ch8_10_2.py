import math


class LazyProperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @LazyProperty
    def area(self):
        print("Computing area")
        return math.pi * self.radius**2

    @LazyProperty
    def perimeter(self):
        print("computing perimeter")
        return 2 * math.pi * self.radius


if __name__ == "__main__":
    c = Circle(4.0)
    print(vars(c))

    print(c.radius)
    print(c.area)
    print(c.area)

    print(c.perimeter)
    print(c.perimeter)

    print(vars(c))

    del c.area
    print(vars(c))
    print(c.area)
    print(vars(c))

    c.area = 25
    print(c.area)
