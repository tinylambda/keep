import trace
from trace_example.recurse import recurse


if __name__ == "__main__":
    tracer = trace.Trace(count=True, trace=False)
    tracer.runfunc(recurse, 2)

    results = tracer.results()
    results.write_results(coverdir="coverdir2")
