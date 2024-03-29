import sys

if __name__ == "__main__":
    if sys.flags.bytes_warning:
        print("Warning on bytes/str errors")
    if sys.flags.debug:
        print("Debugging")
    if sys.flags.inspect:
        print("Will enter interactive mode after running")
    if sys.flags.optimize:
        print("Optimizing byte-code")
    if sys.flags.dont_write_bytecode:
        print("Not writing byte-code files")
    if sys.flags.no_site:
        print('Not importing "site"')
    if sys.flags.ignore_environment:
        print("Ignoring environment")
    if sys.flags.verbose:
        print("Verbose mode")
