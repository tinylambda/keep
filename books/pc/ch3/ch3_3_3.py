if __name__ == "__main__":
    x = 1234.5678
    print(format(x, "0.1f"))

    print(format(-x, "0.1f"))

    print("-" * 64)

    swap_separators = {ord("."): ",", ord(","): "."}
    print(format(x, ",").translate(swap_separators))

    print("-" * 64)
    print("%0.2f" % x)
    print("%10.1f" % x)
    print("%-10.1f" % x)
