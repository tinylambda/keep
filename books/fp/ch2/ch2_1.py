if __name__ == "__main__":
    symbols = "Hello world"
    codes = []

    for symbol in symbols:
        codes.append(ord(symbol))
    print(codes)

    codes = [ord(symbol) for symbol in symbols]
    print(codes)
