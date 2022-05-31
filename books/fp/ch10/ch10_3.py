class MySeq:
    def __getitem__(self, item):
        return item


if __name__ == "__main__":
    s = MySeq()
    print(s[1:4])

    print(s[1:4:2])

    print(s[1:4:2, 9])

    print(s[1:4:2, 7:9])

    print(dir(slice))

    help(slice.indices)

    print(s[1, 2])
