import trace
from trace_example.recurse import recurse


if __name__ == '__main__':
    tracer = trace.Trace(count=False, trace=True)
    tracer.runfunc(recurse, 2)
