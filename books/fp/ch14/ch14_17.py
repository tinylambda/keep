import itertools
import operator


if __name__ == '__main__':
    sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
    print(
        list(itertools.accumulate(sample))
    )

    print(
        list(itertools.accumulate(sample, min))
    )

    print(
        list(itertools.accumulate(sample, max))
    )

    print(
        list(itertools.accumulate(sample, operator.mul))
    )

    print(
        list(itertools.accumulate(range(1, 11), operator.mul))
    )