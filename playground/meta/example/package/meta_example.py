class BlueprintMeta(type):
    def __new__(mcs, name, bases, class_dict):
        print(name, bases, class_dict)
        cls = type.__new__(mcs, name, bases, class_dict)
        return cls

