if __name__ == "__main__":
    items = [0, 1, 2, 3, 4, 5, 6]
    a = slice(2, 4)
    print(items[2:4])
    print(items[a])

    items[a] = [10, 11]
    print(items)

    del items[a]
    print(items)

    a = slice(5, 50, 2)
    print(a.start, a.stop, a.step)

    s = "HelloWorld"
    print(a.indices(len(s)))
    for i in range(*a.indices(len(s))):
        print(i, s[i])
