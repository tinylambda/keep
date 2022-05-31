import copy
import math


class _DictWrapper:
    def __init__(self, values=None, name=""):
        self.name = name
        self.d = {}

        self.log = False

        if values is None:
            return

        init_methods = [
            self.InitPmf,
            self.InitMapping,
            self.InitSequence,
            self.InitFailure,
        ]

        for method in init_methods:
            try:
                method(values)
                break
            except AttributeError:
                continue

        if len(self) > 0:
            self.Normalize()

    def Set(self, x, y=0):
        self.d[x] = y

    def Items(self):
        return self.d.items()

    def InitSequence(self, values):
        for value in values:
            self.Set(value, 1)

    def InitMapping(self, values):
        for value, prob in values.Items():
            self.Set(value, prob)

    def InitPmf(self, values):
        for value, prob in values.Items():
            self.Set(value, prob)

    def InitFailure(self, values):
        raise ValueError("None of the initialization methods worked")

    def __len__(self):
        return len(self.d)

    def __iter__(self):
        return iter(self.d)

    def keys(self):
        return iter(self.d)

    def __contains__(self, item):
        return item in self.d

    def Copy(self, name=None):
        new = copy.copy(self)
        new.d = copy.copy(self.d)
        new.name = name if name is not None else self.name
        return new

    def Scale(self, factor):
        new = self.Copy()
        new.d.clear()

        for val, prob in self.Items():
            new.Set(val * factor, prob)

        return new

    def Log(self, m=None):
        if self.log:
            raise ValueError("Pmf/Hist already under a log transform")
        self.log = True

        if m is None:
            m = self.MaxLike()

        for x, p in self.d.items():
            if p:
                self.Set(x, math.log(p / m))
            else:
                self.Remove(x)

    def Exp(self, m=None):
        if not self.log:
            raise ValueError("Pmf/Hist not under a log transform")
        self.log = False

        if m is None:
            m = self.MaxLike()

        for x, p in self.d.items():
            self.Set(x, math.exp(p - m))

    def GetDict(self):
        return self.d

    def SetDict(self, d):
        self.d = d

    def Values(self):
        return self.d.values()

    def Items(self):
        return self.d.items()

    def Render(self):
        return zip(*sorted(self.Items()))

    def MaxLike(self):
        return max(self.d.values())

    def Print(self):
        for val, prob in sorted(self.d.items()):
            print(val, prob)

    def Remove(self, x):
        del self.d[x]

    def Total(self):
        total = sum(self.d.values())
        return total

    def Incr(self, x, term=1):
        self.d[x] = self.d.get(x, 0) + term

    def Mult(self, x, factor):
        self.d[x] = self.d.get(x, 0) * factor


class Hist(_DictWrapper):
    def Freq(self, x):
        return self.d.get(x, 0)

    def Freqs(self, xs):
        return [self.Freq(x) for x in xs]

    def IsSubset(self, other):
        for val, freq in self.Items():
            if freq > other.Freq(val):
                return False
        return True


class Pmf(_DictWrapper):
    def Prob(self, x, default=0):
        return self.d.get(x, default)

    def Probs(self, xs):
        return [self.Prob(x) for x in xs]
