from operator import methodcaller


if __name__ == "__main__":
    s = "The time has come"
    upcase = methodcaller("upper")
    print(upcase(s))

    hiphenate = methodcaller("replace", " ", "-")
    print(hiphenate(s))
