class Foo:
    def __getitem__(self, item):
        return range(0, 30, 10)[item]


if __name__ == '__main__':
    f = Foo()
    print(f[1])

    for i in f:
        print(i)

    print(
        20 in f,
        15 in f
    )

