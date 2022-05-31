import importlib
import json


class MyEncoder(json.JSONDecoder):
    def __init__(self):
        super(MyEncoder, self).__init__(object_hook=self.dict_to_object)

    def dict_to_object(self, d):
        if "__class__" in d:
            class_name = d.pop("__class__")
            module_name = d.pop("__module__")
            module = importlib.import_module(module_name)
            print("MODULE: ", module.__name__)
            class_ = getattr(module, class_name)
            print("CLASS: ", class_)
            args = {key: value for key, value in d.items()}
            print("INSTANCE ARGS: ", args)
            inst = class_(**args)
        else:
            inst = d
        return inst


encoded_object = """{"__class__": "MyObj", "__module__": "module_json.json_myobj", "s": "internal data"}"""
myobj_instance = MyEncoder().decode(encoded_object)
print(myobj_instance)
