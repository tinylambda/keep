import importlib
import json
import module_json.json_myobj as json_myobj


obj = json_myobj.MyObj("instance value goes here")

print("First attempt")
try:
    print(json.dumps(obj))
except TypeError as err:
    print("ERROR: ", err)


def convert_to_builtin_type(obj):
    print("default(", repr(obj), ")")
    # Convert objects to a dictionary of their representation
    d = {
        "__class__": obj.__class__.__name__,
        "__module__": obj.__module__,
    }
    d.update(obj.__dict__)
    return d


print()
print("With default")
d = json.dumps(obj, default=convert_to_builtin_type)
print(d)

print("Restore")
d_dict = json.loads(d)
mod = importlib.import_module(d_dict["__module__"])
print(mod)
cls = getattr(mod, d_dict["__class__"])
print(cls)
