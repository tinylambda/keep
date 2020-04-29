import inspect
import module_inspect.example as example


for name, data in inspect.getmembers(example):
    if name.startswith('__'):
        continue
    print('{} : {!r}'.format(name, data))

