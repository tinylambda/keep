import collections


class Text(collections.UserString):
    def __repr__(self):
        return "Text({!r})".format(self.data)

    def reverse(self):
        return self[::-1]


if __name__ == "__main__":
    word = Text("forward")
    print(word)
    print(word.reverse())

    print(Text.reverse(Text("backward")))

    print(type(Text.reverse), type(word.reverse))

    print(Text.reverse.__get__(word), Text.reverse.__get__(None, Text))

    print(word.reverse)
    print(word.reverse.__self__)

    print(word.reverse.__func__ is Text.reverse)
