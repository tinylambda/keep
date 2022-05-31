import abc


class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable):
        """Add elements"""

    @abc.abstractmethod
    def pick(self):
        """delete element and return it randomly"""

    def loaded(self):
        return bool(self.inspect())

    def inspect(self):
        """return ordered elements exists"""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))


if __name__ == "__main__":

    class Fake(Tombola):
        def pick(self):
            return 13

    print(Fake)
    f = Fake()  # Error
