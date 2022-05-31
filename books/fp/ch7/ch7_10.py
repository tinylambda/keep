series = []
b = 6


def make_averager():
    # series = []
    b = 7

    def averager(new_value):
        series.append(new_value)
        b = 7
        total = sum(series)
        return total / len(series)

    return averager


if __name__ == "__main__":
    avg = make_averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))

    print(b)
