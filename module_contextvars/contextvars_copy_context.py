from contextvars import Context, copy_context

if __name__ == '__main__':
    """
    Context:

    A mapping of ContextVars to their values.

    Context() creates an empty context with no values in it.
    To get a copy of the current context use the copy_context() function.

    Context implements the collections.abc.Mapping interface.
    """
    ctx: Context = copy_context()
    print(list(ctx.items()))
