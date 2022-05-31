from books.fp.ch16.ch16_7 import demo_exc_handling
from books.fp.ch16.ch16_7 import DemoException


if __name__ == "__main__":
    exc_coro = demo_exc_handling()
    next(exc_coro)
    exc_coro.send(11)
    exc_coro.throw(DemoException)
    exc_coro.send(22)
    from inspect import getgeneratorstate

    print(getgeneratorstate(exc_coro))
