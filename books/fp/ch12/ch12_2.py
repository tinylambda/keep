class AnswerDict(dict):
    def __getitem__(self, item):
        return 42


if __name__ == "__main__":
    ad = AnswerDict(a="foo")
    print(ad["a"])

    d = {}
    d.update(ad)
    print(d)
    print(d["a"])
