from fp.ch16.ch16_11 import averager


if __name__ == '__main__':
    coro_avg = averager()
    next(coro_avg)
    coro_avg.send(10)
    coro_avg.send(30)
    coro_avg.send(6.5)
    try:
        coro_avg.send(None)
    except StopIteration as exc:
        result = exc.value

    print(
        result
    )

