class Demo:
    @classmethod
    def klassmeth(*args):
        return args

    @staticmethod
    def staticmeth(*args):
        return args


if __name__ == '__main__':
    print(
        Demo.klassmeth()
    )
    print(
        Demo.klassmeth('spam')
    )
    print(
        Demo.staticmeth()
    )
    print(
        Demo.staticmeth('spam')
    )

