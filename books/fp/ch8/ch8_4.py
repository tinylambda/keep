if __name__ == "__main__":
    import copy

    a = [10, 20]
    b = [a, 30]
    a.append(b)
    print(a)

    c = copy.deepcopy(a)
    print(c)
