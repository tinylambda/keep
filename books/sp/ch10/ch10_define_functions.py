import dis


def x():
    return 42


dis.dis(x)

print("-" * 64)


def x():
    def y():
        return 42

    return y()


dis.dis(x)

print("-" * 64)


def x():
    a = 42

    def y():
        return a

    return y()


dis.dis(x)
