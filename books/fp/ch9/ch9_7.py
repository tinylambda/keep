from books.fp.ch9.ch9_1 import Vector2d


if __name__ == '__main__':
    v1 = Vector2d(3, 4)
    print(
        hash(v1)
    )
    v2 = Vector2d(3.1, 4.2)
    print(
        hash(v2)
    )

    print(
        set([v1, v2])
    )

    print(v1.__dict__)

