import contextlib


def callback(*args, **kwargs):
    print("closing callback({}, {})".format(args, kwargs))


try:
    with contextlib.ExitStack() as stack:
        stack.callback(callback, "arg1", "arg2")
        stack.callback(callback, arg3="arg3")
        raise RuntimeError("thrown error")
except RuntimeError as err:
    print("ERROR: {}".format(err))
