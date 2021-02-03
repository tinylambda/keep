class DoppelDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


if __name__ == '__main__':
    dd = DoppelDict(one=1)
    print(dd)  # wont call user defined __setitem__

    dd['two'] = 2
    print(dd)  # OK

    dd.update(three=3)
    print(dd)  # wont call user defined __setitem__

