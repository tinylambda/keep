import contextlib


with contextlib.ExitStack() as stack:

    @stack.callback
    def inline_cleanup():
        print("inline_cleanup()")
        print("local_resource = {!r}".format(local_resource))

    local_resource = "resource created in context"
    print("within the context")

# Callbacks make a convenient way to clearly define cleanup logic without the overhead of
# creating a new context manager class. To improve code readability, that logic can be encapsulated in an inline
# function, and callback() can be used as a decorator.
