def simple_coroutine2(a):
    print('-> Started: a =', a)
    b = yield a
    print('-> Received: b =', b)
    c = yield a + b
    print('-> Receid: c =', c)


if __name__ == '__main__':
    my_coro2 = simple_coroutine2(14)
    from inspect import getgeneratorstate
    print(
        getgeneratorstate(my_coro2)
    )

    next(my_coro2)
    print(getgeneratorstate(my_coro2))

    try:
        my_coro2.send(28)
        my_coro2.send(99)
    except StopIteration:
        print(getgeneratorstate(my_coro2))

