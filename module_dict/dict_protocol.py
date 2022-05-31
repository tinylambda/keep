class DictProtocol:
    def __init__(self):
        self.real_data = {}

    def __getitem__(self, item):
        return self.real_data[item]

    def __setitem__(self, key, value):
        self.real_data[key] = value

    def __contains__(self, item):
        return item in self.real_data


if __name__ == "__main__":
    dp = DictProtocol()
    dp["a"] = 100
    dp["b"] = 200

    print(dp["a"])
    print(dp["b"])

    print("a" in dp)
