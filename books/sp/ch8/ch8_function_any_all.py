if __name__ == '__main__':
    mylist = [0, 1, 3, -1]
    if all(map(lambda x: x > 0, mylist)):
        print('all items are greater than 0')

    if any(map(lambda x: x > 0, mylist)):
        print('at least one item is greater than 0')

