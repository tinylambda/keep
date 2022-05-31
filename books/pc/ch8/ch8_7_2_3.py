class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        if name.startswith("_"):
            super(Proxy, self).__setattr__(name, value)
        else:
            setattr(self._obj, name, value)
