if __name__ == '__main__':
    items = [-1, 0, 1, 2]
    # first > 0
    x = list(filter(lambda x: x > 0, items))[0]
    print(x)

    x = next(filter(lambda x: x > 0, items))
    print(x)

    items = []
    x = next((item for item in items if item > 0), '-1')
    print(x)

    from first import first
    print(first([0, False, None, [], (), 42]))
    print(first([-1, 0, 1, 2]))
    print(first([-1, 0, 1, 2], key=lambda item: item > 0))

