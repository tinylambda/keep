if __name__ == "__main__":
    # without list comp
    x = []
    for i in (1, 2, 3):
        x.append(i)
    print(x)

    # with list comp
    x = [i for i in (1, 2, 3)]
    print(x)

    # with list comp multiple
    x = [
        word.capitalize()
        for line in ("hello world?", "world!", "or not")
        for word in line.split()
        if not word.startswith("or")
    ]
    print(x)

    # build a dict
    x = {item: item.upper() for item in ["hello", "world"]}
    print(x)

    # build a set
    x = {item.upper() for item in ["hello", "world"]}
    print(x)
