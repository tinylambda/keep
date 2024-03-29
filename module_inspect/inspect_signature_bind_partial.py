import inspect

import module_inspect.example as example

sig = inspect.signature(example.module_level_function)
partial = sig.bind_partial("this is arg1")

print("Without defaults: ")
for name, value in partial.arguments.items():
    print("{} = {!r}".format(name, value))

print("\nWith defaults: ")
partial.apply_defaults()
for name, value in partial.arguments.items():
    print("{} = {!r}".format(name, value))
