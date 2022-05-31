if __name__ == "__main__":
    symbols = "中方制裁涉台表现恶劣的美方官员"
    beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
    print(beyond_ascii)

    beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
    print(beyond_ascii)
