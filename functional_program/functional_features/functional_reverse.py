from typing import Iterator


def digits(x: int, b: int) -> Iterator[int]:
    if x == 0:
        return
    yield x % b
    for d in digits(x // b, b):
        yield d


def to_base(x: int, b: int) -> Iterator[int]:
    return reversed(tuple(digits(x, b)))


if __name__ == "__main__":
    a = to_base(8, 2)
    print(list(a))
