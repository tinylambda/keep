import inspect


def mygenerator():
    yield 1


if __name__ == '__main__':
    print(inspect.isgeneratorfunction(mygenerator))
    print(inspect.isgeneratorfunction(sum))

    print(inspect.isgenerator(mygenerator))
    print(inspect.isgenerator(mygenerator()))

    gen = mygenerator()
    print(inspect.getgeneratorstate(gen))
    next(gen)
    print(inspect.getgeneratorstate(gen))
    try:
        next(gen)
    except StopIteration:
        pass
    print(inspect.getgeneratorstate(gen))

