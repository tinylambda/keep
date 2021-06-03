class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('expected a string')
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError('cannot delete attribute')


