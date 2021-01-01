class A:
    def __init__(self, value=0):
        self.value = value

    def __add__(self, other):
        if isinstance(other, int):
            self.value += other


if __name__ == '__main__':
    a = A(100)
    a + 100
    print(a.value)

