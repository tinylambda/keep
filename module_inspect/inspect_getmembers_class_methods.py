import inspect
from pprint import pprint

import module_inspect.example as example


pprint(inspect.getmembers(example.A, inspect.isfunction))
