import base64


if __name__ == '__main__':
    s = b'hello'
    a = base64.b64encode(s)
    print(a)

    print(base64.b64decode(a))

    a = base64.b64encode(s).decode('ascii')
    print(a)

