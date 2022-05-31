import contextlib


def callback(*args, **kwargs):
    print("closing callback({}, {})".format(args, kwargs))


with contextlib.ExitStack() as stack:
    stack.callback(callback, "arg1", "arg2")
    stack.callback(callback, arg3="arg3")
