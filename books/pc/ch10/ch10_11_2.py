from urllib.request import urlopen


if __name__ == '__main__':
    u = urlopen('http://127.0.0.1:15000/fib.py')
    data = u.read().decode('utf-8')
    print(data)
