import json
from dataclasses import dataclass
from dataclasses import asdict

if __name__ == "__main__":
    data = {"name": "ACME", "shares": 100, "price": 542.23}

    json_str = json.dumps(data)
    print(json_str)

    data = json.loads(json_str)
    print(data)

    with open("/tmp/data.json", "w") as f:
        json.dump(data, f)

    with open("/tmp/data.json") as f:
        data = json.load(f)
        print(data)

    print(json.dumps(None))
    print(json.dumps(True))
    print(json.dumps(False))

    d = {"a": True, "b": "Hello", "c": None}

    print(json.dumps(d))

    s = '{"name": "ACME", "shares": 100, "price": 542.23}'
    from collections import OrderedDict

    data = json.loads(s, object_pairs_hook=OrderedDict)
    print(data)

    class JSONObject:
        def __init__(self, d):
            self.__dict__ = d

    data = json.loads(s, object_hook=JSONObject)
    print(data.name)
    print(data.shares)
    print(data.price)

    data = {"name": "ACME", "shares": 100, "price": 542.23}
    print(json.dumps(data))
    print(json.dumps(data, indent=4))
    print(json.dumps(data, sort_keys=True))

    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    @dataclass
    class A:
        x: int
        y: int

    p = Point(2, 3)
    # print(json.dumps(p))

    a = A(1, 2)
    print(json.dumps(asdict(a)))

    def serialize_instance(obj):
        d = {"__classname__": type(obj).__name__}
        d.update(vars(obj))
        return d

    classes = {"Point": Point}

    def unserialize_object(d):
        clsname = d.pop("__classname__")
        if clsname:
            cls = classes[clsname]
            obj = cls.__new__(cls)
            for key, value in d.items():
                setattr(obj, key, value)
            return obj
        else:
            return d

    s = json.dumps(p, default=serialize_instance)
    print(s)

    a = json.loads(s, object_hook=unserialize_object)
    print(a.x, a.y)
