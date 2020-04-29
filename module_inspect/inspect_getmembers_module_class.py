import inspect
import module_inspect.example as example

# use predicate argument to filter on the types
for name, data in inspect.getmembers(example, predicate=inspect.isclass):
    print('{}: {!r}'.format(name, data))

