import collections


class DoppelDict2(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


class AnswerDict2(collections.UserDict):
    def __getitem__(self, item):
        return 42


if __name__ == '__main__':
    dd = DoppelDict2(one=1)
    print(dd)

    dd['two'] = 2
    print(dd)

    dd.update(three=3)
    print(dd)

    ad = AnswerDict2(a='foo')
    print(ad)
    print(ad['a'])

    d = {}
    d.update(ad)
    print(d['a'])
    print(d)

