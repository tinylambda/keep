import json
import module_json.json_myobj as json_myobj


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        print("default(", repr(obj), ")")
        # Convert objects to a dictionary of their representation
        d = {
            "__class__": obj.__class__.__name__,
            "__module__": obj.__module__,
        }
        d.update(obj.__dict__)
        return d


obj = json_myobj.MyObj("internal data")
print(obj)
print(MyEncoder().encode(obj))

# another way to use encoder
print(json.dumps(obj, cls=MyEncoder))
