import functools
import inspect
from pprint import pprint


@functools.total_ordering
class MyObject:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        print("testing __eq__({}, {})".format(self.val, other.val))
        return self.val == other.val

    def __gt__(self, other):
        print("testing __gt__({}, {})".format(self.val, other.val))
        return self.val > other.val


print("Methods:\n")
pprint(inspect.getmembers(MyObject, inspect.isfunction))

a = MyObject(1)
b = MyObject(2)

print("\nComparisons: ")
for expr in ["a < b", "a <= b", "a == b", "a >= b", "a > b"]:
    print("\n{:<6}:".format(expr))
    result = eval(expr)
    print("result of {}: {}".format(expr, result))

# The class must provide implementation of __eq__() and one other rich comparison method. The decorator
# adds implementations of the rest of the methods that work by using the comparisons provided.
