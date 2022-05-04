from contextvars import ContextVar, copy_context

var = ContextVar('var')
var.set('spam')


def main():
    # 'var' was set to 'spam' before
    # calling 'copy_context()' and 'ctx.run(main)', so:
    # var.get() == ctx[var] == 'ham'
    var.set('ham')

    # Now, after setting 'var' to 'ham':
    # var.get() == ctx[var] == 'ham'


ctx = copy_context()
print(list(ctx.items()))
# Any changes that the 'main' function makes to 'var'
# will be contained in 'ctx'.
print(f'Before main var.get() = {var.get()}, ctx[var] = {ctx[var]}')
ctx.run(main)
# The 'main()' function was run in the 'ctx' context,
# so changes to 'var' are contained in it:
# ctx[var] == 'ham'

# However, outside of 'ctx', 'var' is still set to 'spam':
# var.get() == 'spam'
print(f'After main var.get() = {var.get()}, ctx[var] = {ctx[var]}')
