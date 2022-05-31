from typing import Callable, Iterable, Tuple, Iterator, Any


Conv_F = Callable[[float], float]
Leg = Tuple[Any, Any, Any]


def convert(conversion: Conv_F, trip: Iterable[Leg]) -> Iterator[float]:
    return (conversion(distance) for start, end, distance in trip)


to_miles = lambda nm: nm * 5280 / 6076.12
to_km = lambda nm: nm * 1.852
to_nm = lambda nm: nm


trip: Leg = ((1.0, 2.0, 3.0), (4.0, 5.0, 6.0))

r = convert(to_miles, trip)
print(list(r))

fst = lambda x: x[0]
snd = lambda x: x[1]
sel2 = lambda x: x[2]

to_miles_2 = lambda s_e_d: to_miles(sel2(s_e_d))
r2 = (to_miles_2(s_e_d) for s_e_d in trip)
print(list(r2))


Point = Tuple[float, float]
Leg_Raw = Tuple[Point, Point]
Point_Func = Callable[
    [Point, Point], float
]  # function to calculate distance between two points
Leg_P_D = Tuple[Leg_Raw, ...]


def cons_distance3(
    distance: Point_Func, legs_iter: Iterable[Leg_Raw]
) -> Iterator[Leg_P_D]:
    return (leg + (round(distance(*leg), 4)) for leg in legs_iter)


r3 = cons_distance3(to_miles_2, trip)
print(list(r3))
