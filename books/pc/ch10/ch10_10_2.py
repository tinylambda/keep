import importlib


if __name__ == "__main__":
    math = importlib.import_module("math")
    print(math.sin(2))
    mod = importlib.import_module("urllib.request")
    print(mod.urlopen("http://www.baidu.com/").read())
