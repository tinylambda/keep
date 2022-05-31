import typing
from dataclasses import dataclass
from dataclasses import field


class C:
    x = []

    def add(self, element):
        self.x.append(element)


@dataclass
class D:
    x: typing.List = field(default_factory=list)

    def add(self, element):
        self.x.append(element)


if __name__ == "__main__":
    o1 = C()
    o2 = C()
    o1.add(1)
    o2.add(2)
    assert o1.x == [1, 2]
    assert o1.x is o2.x

    d1 = D()
    d2 = D()
    d1.add(1)
    d2.add(2)

    print(d1.x)
    print(d2.x)

    assert d1.x is not d2.x
