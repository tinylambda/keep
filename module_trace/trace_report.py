import trace
from trace_example.recurse import recurse


if __name__ == "__main__":
    tracer = trace.Trace(count=True, trace=False, outfile="trace_report.dat")
    tracer.runfunc(recurse, 2)

    report_tracer = trace.Trace(count=False, trace=False, infile="trace_report.dat")
    results = tracer.results()
    results.write_results(summary=True, coverdir="/tmp/")
