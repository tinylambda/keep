def sample():
    yield "Is"
    yield "Chicago"
    yield "Not"
    yield "Chicago?"


print("".join(sample()))


def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield "".join(parts)
            parts = []
            size = 0
    yield "".join(parts)


for part in combine(sample(), 32768):
    # f.write(part)
    print("writing ", part)
