import functools


def deco(f):
    def decorated():
        print("hello")

    return decorated


def deco2(f):
    @functools.wraps(f)
    def decorated():
        print("hello")

    return decorated


@deco
async def coro():
    pass


@deco2
async def coro2():
    pass


if __name__ == "__main__":
    print(coro.__name__)
    print(coro2.__name__)
