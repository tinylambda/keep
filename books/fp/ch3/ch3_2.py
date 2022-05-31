if __name__ == "__main__":
    tt = (1, 2, (30, 40))
    print(hash(tt))

    tf = (1, 2, frozenset([30, 40]))
    print(hash(tf))

    tl = (1, 2, [30, 40])
    print(hash(tl))
