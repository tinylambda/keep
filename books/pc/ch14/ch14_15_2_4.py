class SomeClass:
    def __init__(self):
        self.x = 0

    def method(self, n):
        while n > 0:
            self.x += 1
            n -= 1


if __name__ == "__main__":
    c = SomeClass()
    c.method(1000000)

# time python books/pc/ch14/ch14_15_2_4.py
