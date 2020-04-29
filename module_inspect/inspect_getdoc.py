import inspect

import module_inspect.example as example


print('B.__doc__')
print(example.B.__doc__)

print()

print('getdoc(B)')
print(inspect.getdoc(example.B))

