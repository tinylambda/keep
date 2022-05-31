import contextlib


class Tracker:
    """Base class for noisy context managers."""

    def __init__(self, i):
        self.i = i

    def msg(self, s):
        print("{}({}): {}".format(self.__class__.__name__, self.i, s))

    def __enter__(self):
        self.msg("entering")


class HandleError(Tracker):
    """If an exception is received, treat it as handled."""

    def __exit__(self, exc_type, exc_val, exc_tb):
        received_exc = exc_val is not None
        if received_exc:
            self.msg("handling exception {!r}".format(exc_val))
        self.msg("exiting {}".format(received_exc))
        # Return boolean value indicating whether the exception was handled.
        return received_exc


class PassError(Tracker):
    """If an exception is received, propagate it."""

    def __exit__(self, exc_type, exc_val, exc_tb):
        received_exc = exc_val is not None
        if received_exc:
            self.msg("passing exception {!r}".format(exc_val))
        self.msg("exiting")
        # Return False, indicating any exception was not handled
        return False


class ErrorOnExit(Tracker):
    """Cause an exception."""

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.msg("throw error")
        raise RuntimeError("from {}".format(self.i))


class ErrorOnEnter(Tracker):
    """Cause an exception."""

    def __enter__(self):
        self.msg("throwing error on enter")
        raise RuntimeError("from {}".format(self.i))

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.msg("exiting")


def variable_stack(ctxs):
    with contextlib.ExitStack() as stack:
        for ctx in ctxs:
            stack.enter_context(ctx)


print("No errors: ")
variable_stack(
    [
        HandleError(1),
        PassError(2),
    ]
)

print("\nError at the end of the context stack:")
variable_stack(
    [
        HandleError(1),
        HandleError(2),
        ErrorOnExit(3),
    ]
)

print("\nError in the middle of the context stack: ")
variable_stack(
    [
        HandleError(1),
        PassError(2),
        ErrorOnExit(3),
        HandleError(4),
    ]
)

try:
    print("\nError ignored: ")
    variable_stack(
        [
            PassError(1),
            ErrorOnExit(2),
        ]
    )
except RuntimeError:
    print("error handled outside of context")
