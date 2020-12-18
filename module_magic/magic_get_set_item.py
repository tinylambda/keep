class A:
    def __getitem__(self, item):
        print(f'Getting {item}')

    def __setitem__(self, key, value):
        print(f'setting key {key} to value {value}')


if __name__ == '__main__':
    a = A()
    v = a['x']
    print(v)

    a['x'] = 200
    print(a['x'])

