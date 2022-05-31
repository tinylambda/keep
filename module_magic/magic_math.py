class M:
    def __add__(self, other):
        print("in add with", other)

    def __sub__(self, other):
        print("in sub with", other)

    def __mul__(self, other):
        print("in mul with", other)

    def __divmod__(self, other):
        print("in divmod with", other)


if __name__ == "__main__":
    m1 = M()
    m2 = M()
    m1 + m2
    m1 - m2
    m1 * m2
    divmod(m1, m2)
