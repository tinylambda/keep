from typing import Iterator, Any, Iterable, TypeVar, Tuple

T_ = TypeVar("T_")
Pairs_iter = Iterator[Tuple[T_, T_]]


def legs(lat_lon_iter: Iterator[T_]) -> Pairs_iter:
    begin = next(lat_lon_iter)
    for end in lat_lon_iter:
        yield begin, end
        begin = end


if __name__ == "__main__":
    # l = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
    l = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7] * 1000  # no maximum recursion depth.
    for item in legs(iter(l)):
        print(item)
