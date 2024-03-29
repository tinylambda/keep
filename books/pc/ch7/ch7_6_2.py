if __name__ == "__main__":
    add = lambda x, y: x + y
    print(add(2, 3))
    print(add("hello", "world"))

    def _add(x, y):
        return x + y

    print(_add(2, 3))
    print(_add("hello", "world"))

    names = ["David Beazley", "Brian Jones", "Raymond Hettinger", "Ned Batchelder"]
    print(sorted(names, key=lambda name: name.split()[-1].lower()))
