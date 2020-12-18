class A:
    def __getattribute__(self, item):
        print(f'Getting {item}')


if __name__ == '__main__':
    a = A()
    getattr(a, 'state.s1')
    a.state.s1  # NoneType object has not attribute 's1'



