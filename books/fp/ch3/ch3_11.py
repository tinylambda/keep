from unicodedata import name


if __name__ == "__main__":
    s = {chr(i) for i in range(32, 256) if "SIGN" in name(chr(i), "")}
    print(s)
