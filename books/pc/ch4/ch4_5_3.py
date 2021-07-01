class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


if __name__ == '__main__':
    cd = CountDown(start=10)
    for item in cd:
        print(item)

    print('-' * 64)

    for item in reversed(cd):
        print(item)

