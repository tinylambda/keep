import random

if __name__ == '__main__':
    random.seed()  # based on system time or os.urandom()
    random.seed(12345)
    random.seed(b'bytedata')

    print([random.random() for _ in range(10)])  # will produce same list every time

