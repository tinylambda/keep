import mymodule
from mymodule import B


if __name__ == "__main__":
    b = B()
    b.spam()
    b.bar()

    isinstance(b, mymodule.a.A)
