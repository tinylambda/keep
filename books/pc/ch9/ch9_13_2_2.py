class NoInstances(type):
    def __call__(cls, *args, **kwargs):
        raise TypeError("cannot instantiate directly")


class Spam(metaclass=NoInstances):
    @staticmethod
    def grok(x):
        print("spam.grok")


if __name__ == "__main__":
    Spam.grok(87)
    s = Spam()  # error
