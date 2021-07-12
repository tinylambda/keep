import operator
import itertools


if __name__ == '__main__':
    a = [{'foo': 'bar'}, {'foo': 'bar', 'x': 42}, {'foo': 'baz', 'y': 43}]
    groupby_items = itertools.groupby(a, operator.itemgetter('foo'))
    print(groupby_items)
    print(list(groupby_items))

    print([(key, list(group)) for key, group in itertools.groupby(a, operator.itemgetter('foo'))])

