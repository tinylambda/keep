import dis


abc = ("a", "b", "c")


def concat_a_1():
    for letter in abc:
        abc[0] + letter


def concat_a_2():
    a = abc[0]
    for letter in abc:
        a + letter


if __name__ == "__main__":
    dis.dis(concat_a_1)
    print("-" * 64)
    dis.dis(concat_a_2)
