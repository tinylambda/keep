if __name__ == "__main__":
    # without enumerate
    mylist = [1, 2, 3, 3, 4]
    i = 0
    while i < len(mylist):
        print("item %d: %s" % (i, mylist[i]))
        i += 1

    # with enumerate
    for i, item in enumerate(mylist):
        print("item %d: %s" % (i, item))
