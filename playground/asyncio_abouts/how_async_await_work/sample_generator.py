def eager_range(up_to):
    sequence = []
    index = 0
    while index < up_to:
        sequence.append(index)
        index += 1
    return sequence


def lazy_range(up_to):
    index = 0
    while index < up_to:
        yield index
        index += 1
