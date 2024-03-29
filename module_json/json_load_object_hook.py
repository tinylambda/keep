import importlib
import json


def dict_to_object(d):
    if "__class__" in d:
        class_name = d.pop("__class__")
        module_name = d.pop("__module__")
        # module = __import__(module_name)
        module = importlib.import_module(module_name)
        print("MODULE: ", module.__name__)
        class_ = getattr(module, class_name)
        args = {key: value for key, value in d.items()}
        print("INSTANCE ARGS: ", args)
        inst = class_(**args)
    else:
        inst = d
    return inst


encoded_object = """{"__class__": "MyObj", "__module__": "module_json.json_myobj", "s": "instance value goes here"}"""
myobj_instance = json.loads(encoded_object, object_hook=dict_to_object)
print(myobj_instance)
