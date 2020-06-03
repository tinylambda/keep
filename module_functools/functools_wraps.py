import functools


def show_details(name, f):
    """Show details of a callable object."""
    print('{}: '.format(name))
    print('object: ', f)
    print('__name__: ', end=' ')
    try:
        print(f.__name__)
    except AttributeError:
        print('(no __name__)')
    print('__doc__', repr(f.__doc__))


def simple_decorator(f):
    @functools.wraps(f)
    def decorated(a='decorated defaults', b=1):
        print('decorated: ', (a, b))
        print(' ', end=' ')
        return f(a, b)
    return decorated


def myfunc(a, b=2):
    """myfunc() is not complicated"""
    print('myfunc: ', (a, b))
    return


# The raw function
show_details('myfunc', myfunc)
myfunc('unwrapped, default b')
myfunc('unwrapped, passing b', 3)

# Wrap explicitly
wrapped_myfunc = simple_decorator(myfunc)
show_details('wrapped_myfunc', wrapped_myfunc)
wrapped_myfunc()
wrapped_myfunc('args to wrapped', 4)
print()


# Wrap with decorator syntax
@simple_decorator
def decorated_myfunc(a, b):
    myfunc(a, b)


show_details('decorated_myfunc', decorated_myfunc)
decorated_myfunc()
decorated_myfunc('args to decorated', 4)

# functools provides a decorator, wraps(), that applies update_wrapper() to the decorated function.

