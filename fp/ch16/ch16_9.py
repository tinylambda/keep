from fp.ch16.ch16_7 import demo_exc_handling
from fp.ch16.ch16_7 import DemoException


if __name__ == '__main__':
    exc_demo = demo_exc_handling()
    next(exc_demo)
    exc_demo.send(11)

    try:
        exc_demo.throw(ZeroDivisionError)
    except Exception as e:
        print(e)

    from inspect import getgeneratorstate
    print(
        getgeneratorstate(exc_demo)
    )

