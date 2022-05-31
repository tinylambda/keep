import inspect

import module_inspect.example as example
from module_inspect.inspect_getclasstree import *

print_class_tree(inspect.getclasstree([example.A, example.B, C, D], unique=True))
