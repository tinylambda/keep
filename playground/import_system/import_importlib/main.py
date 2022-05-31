import importlib


math = importlib.import_module("math")
print(math.sin(2))

# mod = importlib.import_module('urllib.request')
# u = mod.urlopen('http://www.python.org')
# print(u.read())


from playground.import_system import import_importlib

b = importlib.import_module(".b", package=import_importlib.__package__)
print(b)
