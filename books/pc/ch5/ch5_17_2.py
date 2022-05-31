import sys


# sys.stdout.write(b'Hello\n')  # Type error

bytes_written = sys.stdout.buffer.write(b"Hello\n")  # OK
print(bytes_written)
