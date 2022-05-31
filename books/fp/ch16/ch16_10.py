class DemoException(Exception):
    pass


def demo_finally():
    print("-> coroutine started")
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print("*** DemoException  handled, Continuing...")
            else:
                print("-> coroutine received: {!r}".format(x))
    finally:
        print("coroutine ending")


if __name__ == "__main__":
    coro = demo_finally()
    next(coro)
    coro.send(11)
    coro.send(22)
    coro.close()

    from inspect import getgeneratorstate

    print(getgeneratorstate(coro))

    coro.throw(ZeroDivisionError)
