import collections.abc


if __name__ == "__main__":
    item = object()

    print(isinstance(item, collections.abc.Sequence))
    print(isinstance(item, collections.abc.Iterable))
    print(isinstance(item, collections.abc.Sized))
    print(isinstance(item, collections.abc.Mapping))

    from decimal import Decimal
    import numbers

    x = Decimal("3.4")
    print(isinstance(x, numbers.Real))
