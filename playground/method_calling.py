import inspect


class T:
    def m_1(self):
        print(self, 'm1')

    def m_2(self):
        print(self, 'm2')

    def do(self):
        for name in dir(self):
            if name.startswith('m_'):
                v = getattr(self, name)
                if inspect.ismethod(v):
                    v()


if __name__ == '__main__':
    t = T()
    t.do()
