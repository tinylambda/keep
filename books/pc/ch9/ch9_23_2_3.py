def test():
    a = 13
    loc = locals()
    exec("b = a + 1")
    b = loc["b"]
    print(b)


test()
