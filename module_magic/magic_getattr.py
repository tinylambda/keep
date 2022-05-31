class SimpleDictProxy:
    def __init__(self, data: dict = None):
        self._data: dict = data

    def __getattribute__(self, item):
        data_dict = super().__getattribute__("_data")
        if item in data_dict:
            value = data_dict[item]
            if isinstance(value, dict):
                value = SimpleDictProxy.create_proxy(value)
                # setattr(self, item, value)
                return value
            else:
                return value

    def __setattr__(self, key, value):
        try:
            data_dict = super().__getattribute__("_data")
            print(f"can get {key}")
            if key in data_dict:
                data_dict.update({key: value})
        except AttributeError:
            print(f"cannot get {key}")
        super().__setattr__(key, value)

    @classmethod
    def create_proxy(cls, data: dict):
        o = cls(data)
        return o


if __name__ == "__main__":
    role_info = {
        "characters": {
            "c1": {
                "instance_id": "c1",
                "level": 10,
                "exp": 10877,
                "star": 2,
            },
            "c2": {
                "instance_id": "c2",
                "level": 23,
                "exp": 400,
                "star": 4,
            },
        }
    }

    p = SimpleDictProxy.create_proxy(role_info)
    print(p.characters)
    print(p.characters.c1)
    print(p.characters.c1.level)
    p.characters.c1.level += 1
    print(p.characters.c1.level)
    p.characters.c1.level += 1
    print(role_info)

    print("-" * 64)
    print(p.characters.c1.level)
