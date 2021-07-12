if __name__ == '__main__':
    map_items = map(lambda x: x + 'bzz!', ['I think', 'I\'m good'])
    print(map_items)
    print(list(map_items))

    map_items = (x + 'bzz!' for x in ['I think', 'I\'m good'])
    print(map_items)
    print(list(map_items))

