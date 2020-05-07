import weakref


class ExpensiveObject:
    def __del__(self):
        print('(Deleting {})'.format(self))


def callback(reference):
    """Invoked when referenced object is deleted"""
    print('callback({!r})'.format(reference))


obj = ExpensiveObject()

# One use for callback is to remove the weak reference object from a cache.
r = weakref.ref(obj, callback)

print('obj: ', obj)
print('ref: ', r)
print('r(): ', r())

print('deleting obj')
del obj
print('r(): ', r())

