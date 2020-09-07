from typing import TypeVar
from typing import Sequence
from typing import List
from typing import Tuple
from typing import Iterator


ItemType = TypeVar('ItemType')
Flat = Sequence[ItemType]
Grouped = List[Tuple[ItemType, ...]]

Flat_Iter = Iterator[ItemType]
Grouped_iter = Iterator[Tuple[ItemType, ...]]


def group_by_seq(n: int, sequence: Flat) -> Grouped:
    flat_iter = iter(sequence)
    full_sized_items = list(
        tuple(
            (next(flat_iter) for i in range(n)))
        for row in range(len(sequence) // n)
    )

    trailer = tuple(flat_iter)
    if trailer:
        return full_sized_items + [trailer]
    else:
        return full_sized_items


def group_by_iter(n: int, iterable: Flat_Iter) -> Grouped_iter:
    row = tuple(next(iterable) for i in range(n))
    while row:
        yield row
        row = tuple(next(iterable) for i in range(n))


if __name__ == '__main__':
    flat = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, ]
    g = group_by_seq(3, flat)
    print(g)

    flat2 = [1]
    print(list(group_by_iter(3, iter(flat))))

