class M:
    def __getitem__(self, item):
        print(f'You are getting <{item}>')

    def __getattr__(self, item):
        print(f'You are getting attribute <{item}>')


if __name__ == '__main__':
    m = M()
    m['x']
    m.y
