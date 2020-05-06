import traceback
import sys

from module_traceback.traceback_example import call_function


def f():
    summary = traceback.StackSummary.extract(
        traceback.walk_stack(None)
    )
    print(''.join(summary.format()))


print('Calling f() directly:')
f()

print()
print('Calling f() from 3 levels deep:')
call_function(f)

