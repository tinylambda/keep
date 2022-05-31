from dataclasses import dataclass
from dataclasses import field


@dataclass
class C:
    mylist: list[int] = field(default_factory=list)


if __name__ == "__main__":
    c = C()
    c.mylist += [1, 2, 3]
    print(c)
