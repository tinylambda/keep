"""
Wait for notification that an input or output channel is ready

The new selectors module provides a higher-level interface built on top of the APIs in select.
It is easier to build portable code using selectors,
so use that module unless the low-level APIs provided by select are somehow required.

select() makes it easier to monitor multiple connections at the same time,
and is more efficient than writing a polling loop in Python using socket timeouts,
because the monitoring happens in the operating system network layer, instead of the interpreter.

Using Python’s file objects with select() works for Unix, but is not supported under Windows.
"""
