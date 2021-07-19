if __name__ == '__main__':
    s = b'abcdefgh'
    view = memoryview(s)
    print(view[1])
    limited = view[1:3]
    print(limited)
    print(bytes(view[1:3]))
