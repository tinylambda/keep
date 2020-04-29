import inspect

import module_inspect.example as example


class C(object):
    pass


class CFirst(C, example.B):
    pass


class BFirst(example.B, C):
    pass


print('BFirst: ')
for c in inspect.getmro(BFirst):
    print('{}'.format(c.__name__))
print()
print('CFirst')
for c in inspect.getmro(CFirst):
    print('{}'.format(c.__name__))

