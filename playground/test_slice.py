if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 5]
    header, *remaining = test_list
    print(header)
    print(remaining)

    a, b, c, d = remaining
    print(a, b, c, d)
