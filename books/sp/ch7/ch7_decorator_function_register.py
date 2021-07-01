_functions = {}


def register(f):
    global _functions
    _functions[f.__name__] = f


@register
def foo():
    return 'bar'


if __name__ == '__main__':
    print(_functions)

