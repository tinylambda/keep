def sample():
    n = 0

    def func():
        print("n=", n)

    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    func.get_n = get_n
    func.set_n = set_n

    return func


if __name__ == "__main__":
    f = sample()
    f()
    f.set_n(10)
    f()
    print(f.get_n())
