import inspect
from pprint import pprint

import module_inspect.example as example


a = example.A(name='inspect_getmembers')
pprint(
    inspect.getmembers(a, inspect.ismethod)
)

