import os

from urllib.request import urlopen


filename = "spam.txt"
print(filename.endswith(".txt"))
print(filename.startswith("file"))

url = "http://www.python.org"
print(url.startswith("http:"))


filenames = os.listdir("")
print(filenames)
print([name for name in filenames if name.endswith((".c", ".py"))])
print(any(name.endswith(".py") for name in filenames))


def read_data(name):
    if name.startswith(("http:", "https:", "ftp:")):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


choices = ["http:", "ftp:"]
url = "http://www.python.org"
# print(url.startswith(choices))  # must be str or a tuple of str
print(url.startswith(tuple(choices)))
