import itertools
import operator


if __name__ == "__main__":
    ct = itertools.count()
    print(
        next(ct),
        next(ct),
        next(ct),
        next(ct),
        next(ct),
    )

    print(list(itertools.islice(itertools.count(1, 0.3), 3)))

    cy = itertools.cycle("ABC")
    print(next(cy))

    print(list(itertools.islice(cy, 7)))

    rp = itertools.repeat(7)
    print(next(rp), next(rp))

    print(list(itertools.repeat(8, 4)))

    print(list(map(operator.mul, range(11), itertools.repeat(5))))
