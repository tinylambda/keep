from random import randrange

from books.fp.ch11.ch11_5 import Tombola


@Tombola.register
class TomboList(list):
    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from emtpy TomboList')

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))


if __name__ == '__main__':
    print(
        issubclass(TomboList, Tombola)
    )

    t = TomboList(range(100))
    print(
        isinstance(t, Tombola)
    )

