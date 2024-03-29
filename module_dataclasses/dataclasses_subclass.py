import dataclasses
from dataclasses import dataclass
from dataclasses import asdict


@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0


@dataclass
class GoodPoint(Point):
    z: int = 47


class BadPoint(Point):
    z: int = 55


class Common:
    pass


if __name__ == "__main__":
    gp = GoodPoint()  # include z
    d = asdict(gp)
    print(d)

    bp = BadPoint()  # won't include z
    d2 = asdict(bp)
    print(d2)

    print(dataclasses.is_dataclass(gp), dataclasses.is_dataclass(GoodPoint))
    print(dataclasses.is_dataclass(bp), dataclasses.is_dataclass(BadPoint))
    print(dataclasses.is_dataclass(Common()), dataclasses.is_dataclass(Common))
