if __name__ == '__main__':
    symbols = 'Hello world'
    print(tuple(ord(symbol) for symbol in symbols))

    import array
    arr = array.array('I', (ord(symbol) for symbol in symbols))
    print(arr)

