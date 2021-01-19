if __name__ == '__main__':
    s = '四川三例疑似病例'

    u16 = s.encode('utf_16')
    print(u16)
    print(list(u16))

    u16le = s.encode('utf_16le')
    print(u16le)
    print(list(u16le))

    u16be = s.encode('utf_16be')
    print(u16be)
    print(list(u16be))

