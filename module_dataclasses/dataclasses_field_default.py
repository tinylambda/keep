import pprint

from dataclasses import dataclass
from dataclasses import field
from dataclasses import fields


@dataclass
class C:
    x: int
    y: int = field(repr=False)
    z: int = field(repr=False, default=10)
    t: int = 20


if __name__ == '__main__':
    c = C(100, 200)
    print(c.z)
    print(c.t)
    print(c.x, c.y)

    pprint.pprint(fields(C))
    pprint.pprint(fields(c))

