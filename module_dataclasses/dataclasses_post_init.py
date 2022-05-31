from dataclasses import dataclass
from dataclasses import field


@dataclass
class C:
    a: float
    b: float
    c: float = field(init=False)

    def __post_init__(self):
        self.c = self.a + self.b


if __name__ == "__main__":
    c = C(1.0, 2.0)
    print(c)
    print(c.c)
