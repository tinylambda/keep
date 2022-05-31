import sys


# create a binary-mode file for stdout
bstdout = open(sys.stdout.fileno(), "wb", closefd=False)
bstdout.write(b"hello world\n")
bstdout.flush()
