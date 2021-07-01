def identity(f):
    return f


if __name__ == '__main__':
    @identity
    def foo():
        return 'bar'

    # is equal to
    foo = identity(foo)

