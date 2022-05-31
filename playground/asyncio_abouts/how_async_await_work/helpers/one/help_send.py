def writer():
    while True:
        w = yield
        print(">> ", w)


def writer_wrapper(coro):
    coro.send(None)
    while True:
        try:
            x = yield
            coro.send(x)
        except StopIteration:
            pass


def writer_wrapper2(coro):
    yield from coro


if __name__ == "__main__":
    w = writer()
    wrap = writer_wrapper(w)
    wrap.send(None)
    for i in range(4):
        wrap.send(i)

    print("-" * 64)

    wrap2 = writer_wrapper2(w)
    for i in range(4):
        wrap.send(i)
