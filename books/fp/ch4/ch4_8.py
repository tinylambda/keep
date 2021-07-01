if __name__ == '__main__':
    octets = b'Montr\xe9al'

    r = octets.decode('cp1252')
    print(r)

    r = octets.decode('iso8859_7')
    print(r)

    r = octets.decode('koi8_r')
    print(r)

    r = octets.decode('utf-8', errors='replace')
    print(r)
