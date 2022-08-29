class Awaitable:
    def __await__(self):
        value = yield 1
        print("Awaitable received:", value)
        value = yield 2
        print("Awaitable received:", value)
        value = yield 3
        print("Awaitable received:", value)
        return 42


async def foo():
    print("foo start")
    result = await Awaitable()
    print("foo received result:", result)
    print("foo end")


async def bar():
    print("bar start")


if __name__ == "__main__":
    try:
        f_coro = foo()
        f_coro.send(None)
        v = f_coro.send("one")
        print("coro return", v)
        v = f_coro.send("two")
        print("coro return", v)
        v = f_coro.send("three")
        print("coro return", v)
    except Exception as e:
        print("f_coro error", e)

    try:
        b_coro = bar()
        b_coro.send(None)
    except Exception as e:
        print("b_coro error", e)
