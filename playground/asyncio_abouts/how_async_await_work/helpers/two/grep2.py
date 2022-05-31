def grep2(pattern):
    print(f"looking for {pattern}")
    while True:
        line = yield
        if pattern in line:
            print(line)


if __name__ == "__main__":
    g = grep2("python")
    next(g)  # prepare this generator
    g.send("hello")
    g.send("world")
    g.send("python here")
    g.send("go python")
    g.send("bye")
