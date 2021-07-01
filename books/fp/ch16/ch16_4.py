def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


if __name__ == '__main__':
    coro_avg = averager()
    next(coro_avg)
    print(
        coro_avg.send(10)
    )
    print(
        coro_avg.send(30)
    )

    print(
        coro_avg.send(5)
    )

