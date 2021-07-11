import bz2
import contextlib


with bz2.BZ2File('example.bz2', 'rb') as _input:
    print('Entire file:')
    all_data = _input.read()
    print(all_data)

    expected = all_data[5: 15]

    # rewind to beginning
    _input.seek(0)
    # move ahead 5 bytes
    _input.seek(5)
    print('starting at position 5 for 10 bytes:')
    partial = _input.read(10)
    print(partial)

    print()
    print(expected == partial)

