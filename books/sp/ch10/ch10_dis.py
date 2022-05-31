import dis


def x():
    return 42


if __name__ == "__main__":
    dis.dis(x)
