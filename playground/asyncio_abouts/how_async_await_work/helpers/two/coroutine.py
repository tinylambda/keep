def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr

    return start


if __name__ == "__main__":

    @coroutine
    def grep(pattern):
        print(f"looking for {pattern}")
        while True:
            line = yield
            if pattern in line:
                print(line)

    g = grep("python")
    g.send("hello")
    g.send("python go")
