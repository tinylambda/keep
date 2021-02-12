from fp.ch16.ch16_5 import averager


if __name__ == '__main__':
    coro_avg = averager()
    print(coro_avg.send(50))
    print(coro_avg.send(40))

    coro_avg.send('spam')
    coro_avg.send(60)

