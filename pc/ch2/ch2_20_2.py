import re

if __name__ == '__main__':
    data = b'hello world'
    print(data[0:5])
    print(data.startswith(b'hello'))
    print(data.split())
    print(data.replace(b'hello', b'hello cruel'))

    data = bytearray(b'hello world')
    print(data[0:5])
    print(data.startswith(b'hello'))
    print(data.split())
    print(data.replace(b'hello', b'hello cruel'))
    print(data)

    data = b'FOO:BAR,SPAM'
    print(re.split(b'[:,]', data))

