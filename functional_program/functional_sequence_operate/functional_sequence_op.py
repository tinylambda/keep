from typing import Iterator, Any, Tuple

Item_Iter = Iterator[Any]
Pairs_Iter = Iterator[Tuple[float, float]]


def pairs(iterator: Item_Iter) -> Pairs_Iter:
    def pairs_from(head: Any, iterable_tail: Item_Iter) -> Pairs_Iter:
        nxt = next(iterable_tail)
        yield head, nxt
        yield from pairs_from(nxt, iterable_tail)

    try:
        return pairs_from(next(iterator), iterator)
    except StopIteration:
        return iter([])


if __name__ == '__main__':
    l = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
    # l = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7] * 1000  # maximum recursion depth.
    for item in pairs(iter(l)):
        print(item)



