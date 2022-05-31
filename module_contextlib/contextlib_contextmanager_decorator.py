import contextlib


@contextlib.contextmanager
def make_context():
    print("entering")
    try:
        yield
    except RuntimeError as err:
        print("ERROR: ", err)
    finally:
        print("exiting")


@make_context()
def normal():
    print("inside with statement")


@make_context()
def throw_error(err):
    raise err


print("Normal: ")
normal()

print("\nHandled error: ")
throw_error(RuntimeError("showing example of handling an error"))

print("\nUnhandled error")
throw_error(ValueError("this exception is not handled"))

# As in the ContextDecorator example above, when the context manager is used as a decorator the value yielded by the
# generator is not available inside the function being decorated. Arguments passed to the decorated function are still
# available, as demonstrated by throw_error() in this example.
