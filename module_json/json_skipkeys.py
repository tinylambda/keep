import json

data = [{"a": "A", "b": (2, 4), "c": 3.0, ("d",): "D tuple"}]

print("First attempt")
try:
    print(json.dumps(data))
except TypeError as err:
    print("ERROR: ", err)

print()
print("Second attempt")
print(json.dumps(data, skipkeys=True))
