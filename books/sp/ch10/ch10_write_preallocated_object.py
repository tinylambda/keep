if __name__ == '__main__':
    ba = bytearray(8)
    print(ba)

    with open('/dev/urandom', 'rb') as source:
        source.readinto(ba)

    print(ba)

    print('-' * 64)

    ba = bytearray(8)
    ba_at_4 = memoryview(ba)[4:]
    with open('/dev/urandom', 'rb') as source:
        source.readinto(ba_at_4)
    print(ba)
