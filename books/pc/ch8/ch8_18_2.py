from module_logging import logger


class LoggedMappingMixin:
    __slots__ = ()

    def __getitem__(self, item):
        print("getting", str(item))
        return super().__getitem__(item)

    def __setitem__(self, key, value):
        print(f"setting {key} = {value!r}")
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        print("deleting", key)
        return super().__delitem__(key)


class SetOnceMixin:
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(f"{key} already set")
        return super().__setitem__(key, value)


class StringKeysMappingMixin:
    __slots__ = ()

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError("keys must be strings")
        super().__setitem__(key, value)


class LoggedDict(LoggedMappingMixin, dict):
    pass


if __name__ == "__main__":
    d = LoggedDict()
    d["x"] = 23
    d["x"]
    del d["x"]

    logger.info("done")
