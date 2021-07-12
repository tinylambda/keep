if __name__ == '__main__':
    items = [('a', 2), ('c', 1), ('d', 4)]
    sorted_items = sorted(items, key=lambda x: x[1])
    print(sorted_items)

