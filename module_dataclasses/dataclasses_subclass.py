from dataclasses import dataclass
from dataclasses import asdict


@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0


class GoodPoint(Point):
    pass


if __name__ == '__main__':
    gp = GoodPoint()
    d = asdict(gp)
    print(d)

