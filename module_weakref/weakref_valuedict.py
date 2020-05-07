import gc
import weakref

from pprint import pprint


gc.set_debug(gc.DEBUG_UNCOLLECTABLE)


class ExpensiveObject:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'ExpensiveObject({})'.format(self.name)

    def __del__(self):
        print('(Deleting {})'.format(self))


def demo(cache_factory):
    all_refs = {}
    print('CACHE TYPE: ', cache_factory)
    cache = cache_factory()
    for name in ['one', 'two', 'three']:
        o = ExpensiveObject(name)
        cache[name] = o
        all_refs[name] = o
        del o

    print('all_refs = ', end=' ')
    pprint(all_refs)
    print('\nBefore, cache contains: ', list(cache.keys()))
    for name, value in cache.items():
        print('{} = {}'.format(name, value))
        del value

    print('\nCleanup: ')
    del all_refs
    gc.collect()

    print('\nAfter, cache contains: ', list(cache.keys()))
    for name, value in cache.items():
        print('{} = {}'.format(name, value))
    print('demo returning')


demo(dict)
print()
demo(weakref.WeakValueDictionary)

