if __name__ == "__main__":
    t1 = (1, 2, 3)
    t2 = tuple(t1)
    print(t1 is t2)

    t3 = t1[:]
    print(t3 is t1)

    t1 = (1, 2, 3)
    t3 = (1, 2, 3)
    print(t3 is t1)

    s1 = "ABC"
    s2 = "ABC"
    print(s2 is s1)
